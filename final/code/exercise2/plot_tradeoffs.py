"""
Create plots for the trade-offs of the first run of GSEMO for each problem.
"""

import pandas as pd
import matplotlib.pyplot as plt

pids = [2100, 2101, 2102, 2103, 2200, 2201, 2202, 2203, 2300, 2301, 2302]

for pid in pids:
    df = pd.read_csv(f"results_moea/{pid}_GSEMO_tradeoff_first_run.csv")

    x = df["size"]
    y = df["value_f"]

    # Make plots
    plt.plot(x, y, marker='o', label="Pareto front")
    plt.scatter(x, y)

    plt.xlabel("Size")
    plt.ylabel("Function value")
    plt.title(f"F{pid} GSEMO First Run Trade-off (10,000 budget)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"F{pid}_GSEMO_trade-off", dpi=150)
    
    plt.close()
    