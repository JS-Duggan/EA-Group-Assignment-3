import ioh
from ioh import get_problem, ProblemClass, logger
import numpy as np
import random

import multiprocessing
from multiprocessing import Pool
from multiprocessing import Lock
import time

def rls(func, budget=10_000, seed=None):
    """
    Randomized Local Search 
    """
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    n = func.meta_data.n_variables
    
    # Initial solution
    x = np.random.randint(2, size=n)
    f = func(x)
    evals = 1

    while evals < budget and f < func.optimum.y:

        y = x.copy()
        idx = random.randint(0, n - 1)
        y[idx] = 1 - y[idx]
        
        fy = func(y)
        evals += 1
        

        if fy >= f:
            x, f = y, fy
            

    return f, x

# -------- (1+1) Evolutionary Algorithm ----------
def one_plus_one_ea(func, budget=10_000, seed=None):

    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
        
    n = func.meta_data.n_variables
    mutation_rate = 1.0 / n
    

    x = np.random.randint(2, size=n)
    f = func(x)
    evals = 1
    
    while evals < budget and f < func.optimum.y:

        y = bitflip_mutation(x, rate=mutation_rate)
        
        fy = func(y)
        evals += 1
        

        if fy >= f:
            x, f = y, fy
            

    return f, x

# ------- Your Genetic Algorithm  ----------

def uniform_crossover(a, b):
    n = len(a)
    c1, c2 = np.empty(n, dtype=int), np.empty(n, dtype=int)
    for i in range(n):
        if random.random() < 0.5:
            c1[i], c2[i] = a[i], b[i]
        else:
            c1[i], c2[i] = b[i], a[i]
    return c1, c2

def bitflip_mutation(x, rate=0.01):
    y = x.copy()
    for i in range(len(x)):
        if random.random() < rate:
            y[i] = 1 - y[i]
    return y

def tournament_select(pop, fitness, k=3):
    idxs = random.sample(range(len(pop)), k)
    best_idx = max(idxs, key=lambda i: fitness[i])
    return pop[best_idx]

def genetic_algorithm(func, budget=10_000, mu=20, lamb=40, seed=None):
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    n = func.meta_data.n_variables
    mutation_rate = 1.0 / n  


    pop = [np.random.randint(2, size=n) for _ in range(mu)]
    fitness = [func(x) for x in pop]
    evals = len(pop)

    best_idx = int(np.argmax(fitness))
    best_f, best_x = fitness[best_idx], pop[best_idx]


    while evals < budget and best_f < func.optimum.y:
        offspring, off_fitness = [], []
        while len(offspring) < lamb and evals < budget:
            p1 = tournament_select(pop, fitness)
            p2 = tournament_select(pop, fitness)
            c1, c2 = uniform_crossover(p1, p2)


            c1 = bitflip_mutation(c1, mutation_rate)
            f1 = func(c1); evals += 1
            offspring.append(c1); off_fitness.append(f1)

            if evals < budget and len(offspring) < lamb:
                c2 = bitflip_mutation(c2, mutation_rate)
                f2 = func(c2); evals += 1
                offspring.append(c2); off_fitness.append(f2)


        combined = pop + offspring
        combined_fit = fitness + off_fitness
        sorted_idx = np.argsort(combined_fit)[::-1] 
        pop = [combined[i] for i in sorted_idx[:mu]]
        fitness = [combined_fit[i] for i in sorted_idx[:mu]]


        if fitness[0] > best_f:
            best_f, best_x = fitness[0], pop[0]


    return best_f, best_x

def wrapper(args):
    pid, alg_func, alg_name, budget, runs = args
    
    l = logger.Analyzer(
        root="data_ex1",  
        folder_name=f"{alg_name}_runs",
        algorithm_name=alg_name,
        algorithm_info=f"Exercise 1 run for {alg_name}"
    )
    
    problem = ioh.get_problem(pid, problem_class=ProblemClass.GRAPH)
    problem.attach_logger(l)
    # print(f"  Problem: {problem.meta_data.name} (ID: {pid})")
    
    
    
    for r in range(runs):
        checkpoint = time.perf_counter()

        seed = (pid * runs) + r 

        alg_func(problem, budget=budget, seed=seed)
        
        if (r + 1) % 10 == 0:
            print(f"    ... completed run {r+1}/{runs}")
        
        problem.reset()
        
        print(f"Run time (s): {time.perf_counter() - checkpoint:.2f}")

# -------- Driver Code ----------
def run_exercise_1():
    

    problem_ids = [
        2100, 2101, 2102, 2103,  # MaxCoverage
        2200, 2201, 2202, 2203,  # MaxInfluence
        2300, 2301, 2302         # PackWhileTravel
    ]
    
    # Define Algo
    algorithms = {
        "RLS": rls,
        "OnePlusOne_EA": one_plus_one_ea,
        "GA": genetic_algorithm
    }
    

    budget = 100_000
    n_runs = 30
    
    num_workers = multiprocessing.cpu_count()
    runs_per_worker = n_runs // num_workers
    extra_runs = n_runs % num_workers
    
    # --- Run Experiment ---
    for alg_name, alg_func in algorithms.items():
        print(f"\n--- Running Algorithm: {alg_name} ---")
        

        # l = logger.Analyzer(
        #     root="data_ex1",  
        #     folder_name=f"{alg_name}_runs",
        #     algorithm_name=alg_name,
        #     algorithm_info=f"Exercise 1 run for {alg_name}"
        # )
        
        for pid in problem_ids:
            try:
                checkpoint = time.perf_counter()

                problem = ioh.get_problem(pid, problem_class=ProblemClass.GRAPH)
                # problem.attach_logger(l)
                print(f"  Problem: {problem.meta_data.name} (ID: {pid})")
                
                
                all_tasks = []
                for i in range(num_workers):
                    runs = runs_per_worker + (1 if i < extra_runs else 0)
                    if runs > 0:
                        all_tasks.append((pid, alg_func, alg_name, budget, runs))
                        
                with Pool(processes=num_workers) as pool:
                    pool.map(wrapper, all_tasks)
                    
                
                print(f"Total time (s): {time.perf_counter() - checkpoint:.2f}")
                
                # for r in range(n_runs):
                #     print(r)

                #     seed = (pid * n_runs) + r 
                    

                #     alg_func(problem, budget=budget, seed=seed)
                    
                #     if (r + 1) % 10 == 0:
                #         print(f"    ... completed run {r+1}/{n_runs}")
                    

                #     problem.reset() 
                        
            except Exception as e:
                print(f"    ERROR running {alg_name} on {pid}: {e}")
        
        print(f"--- Finished {alg_name} ---")
        # del l 

    print("\nAll algorithms Exercise 1 completed.")
    print(f"Data saved to 'data_ex1' directory.")

if __name__ == "__main__":
    run_exercise_1()
