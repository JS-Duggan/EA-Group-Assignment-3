
from __future__ import annotations
import argparse, random
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import multiprocessing
from multiprocessing import Pool
from multiprocessing import Lock
import time

import numpy as np

lock = Lock()

try:
    import ioh
except Exception as e:
    raise SystemExit("Please install IOH: pip install ioh") from e

def dominates(a: Tuple[float,int], b: Tuple[float,int]) -> bool:
    fa, sa = a
    fb, sb = b
    return (fa >= fb and sa <= sb) and (fa > fb or sa < sb)

@dataclass
class Offspring:
    x: np.ndarray
    f: float
    size: int

class GSEMO:
    def __init__(self, n: int):
        self.n = n
        self.archive: List[Offspring] = []

    def initialize(self, problem) -> None:
        x = np.zeros(self.n, dtype=int)
        f = problem(x)
        self.archive = [Offspring(x=x, f=float(f), size=0)]

    def _mutate(self, x: np.ndarray) -> np.ndarray:
        n = self.n
        p = 1.0 / n
        flips = np.random.rand(n) < p
        if not flips.any():
            flips[np.random.randint(0, n)] = True
        y = x ^ flips.astype(int)
        return y

    def step(self, problem) -> Tuple[float, int]:
        idx = np.random.randint(0, len(self.archive))
        parent = self.archive[idx]
        y = self._mutate(parent.x)
        fy = float(problem(y))
        sy = int(y.sum())

        y_obj = (fy, sy)
        is_dominated = False
        to_remove = []
        for i, ind in enumerate(self.archive):
            a_obj = (ind.f, ind.size)
            if dominates(a_obj, y_obj):
                is_dominated = True
                break
            if dominates(y_obj, a_obj):
                to_remove.append(i)

        if not is_dominated:
            for i in sorted(to_remove, reverse=True):
                del self.archive[i]
            self.archive.append(Offspring(x=y, f=fy, size=sy))

        best_f = max(ind.f for ind in self.archive)
        min_size = min(ind.size for ind in self.archive if ind.f == best_f)
        return best_f, min_size

def run_gsemo_on_problem(problem_id: int, budget: int, runs: int, out_dir: Path, seed_base: int = 12345):    
    out_dir.mkdir(parents=True, exist_ok=True)
    f = ioh.get_problem(problem_id, problem_class=ioh.ProblemClass.GRAPH)
    n = f.meta_data.n_variables

    analyzer_root = out_dir / f"ioh_data_{problem_id}"

    import csv, numpy as np, json
    all_histories = []
    tradeoffs_first_run = []
    
    for r in range(runs):
        checkpoint = time.perf_counter()

        np.random.seed(seed_base + r)
        random.seed(seed_base + r)
        
        analyzer = ioh.logger.Analyzer(root=str(analyzer_root), algorithm_name="GSEMO", store_positions=False)
        f.attach_logger(analyzer)
        
        algo = GSEMO(n)
        algo.initialize(f)
        best_f = max(ind.f for ind in algo.archive)
        history = [best_f]
        for t in range(1, budget):
            best_f, _ = algo.step(f)
            history.append(best_f)
        
        f.detach_logger()
        
        f.reset()

        all_histories.append(history)
        if r == 0:
            tradeoffs_first_run = sorted({(ind.f, ind.size) for ind in algo.archive}, key=lambda p: (p[0], -p[1]))
            
        print(f"Run time (s): {time.perf_counter() - checkpoint:.2f}")

    with lock:
        csv_path = out_dir / f"{problem_id}_GSEMO_fixed_budget.csv"
        with open(csv_path, "w", newline="", encoding="utf-8") as csvf:
            w = csv.writer(csvf)
            w.writerow(["eval", "mean_best_f", "std_best_f"])
            A = np.array(all_histories)
            mean = A.mean(axis=0)
            std = A.std(axis=0, ddof=1) if A.shape[0] > 1 else np.zeros_like(mean)
            for i in range(len(mean)):
                w.writerow([i+1, float(mean[i]), float(std[i])])

        trade_path = out_dir / f"{problem_id}_GSEMO_tradeoff_first_run.csv"
        if not trade_path.exists():
            with open(trade_path, "w", newline="", encoding="utf-8") as csvf:
                w = csv.writer(csvf)
                w.writerow(["value_f", "size"])
                for (fv, sz) in tradeoffs_first_run:
                    w.writerow([float(fv), int(sz)])

    return {
        "problem_id": problem_id,
        "n": n,
        "csv_summary": str(csv_path),
        "tradeoff_csv_first_run": str(trade_path),
        "ioh_dir": str(analyzer_root),
    }
    
def wrapper(args):
    return run_gsemo_on_problem(*args)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=int, default=10000)
    ap.add_argument("--runs", type=int, default=30)
    ap.add_argument("--out_dir", type=str, default="results_moea")
    args = ap.parse_args()
    
    num_workers = multiprocessing.cpu_count()
    runs_per_worker = args.runs // num_workers
    extra_runs = args.runs % num_workers

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    problem_ids = [2100,2101,2102,2103,2200,2201,2202,2203,2300,2301,2302]

    meta = []
    for pid in problem_ids:
        print(f"=== Running GSEMO on problem {pid} (budget={args.budget}, runs={args.runs}) ===", flush=True)
        
        checkpoint = time.perf_counter()
        
        all_tasks = []
        for i in range(num_workers):
            runs = runs_per_worker + (1 if i < extra_runs else 0)
            if runs > 0:
                all_tasks.append((pid, args.budget, runs, out_dir))
       
        with Pool(processes=num_workers) as pool:
            pool.map(wrapper, all_tasks)
            
        
        print(f"Total time (s): {time.perf_counter() - checkpoint:.2f}")
        
        
        # info = run_gsemo_on_problem(pid, args.budget, args.runs, out_dir)
        # meta.append(info)

    # import json
    # with open(out_dir / "meta.json", "w", encoding="utf-8") as jf:
    #     json.dump(meta, jf, indent=2)

if __name__ == "__main__":
    main()
