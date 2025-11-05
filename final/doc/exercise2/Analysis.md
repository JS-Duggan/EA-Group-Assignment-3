# MaxCoverage and MaxInfluence Performance

As seen in the fixed budget plots, the GSEMO algorithm performed significantly better than RLS, (1+1) EA, and GA from exercise 1 on the MaxCoverage and MaxInfluence problem instances. The GSEMO algorithm converged quickest in all MaxCoverage problem instances, while none of the algorithms converged in the MaxInfluence problems for the 10,000 evaluations budget.

For the MaxCoverage problem instances, the GSEMO algorithm performed the best with the fastest convergence. The GSEMO algorithm had a gradual convergence, while the RLS, (1+1) EA, and GA had a sharp increase in fitness between 1,000 and 10,000 evaluations before converging.

For the MaxInfluence problem instances, the GSEMO algorithm maintained a significantly better performance than RLS, (1+1) EA, and GA, with a significantly greater performance gap seperating GSEMO from the other algorithms; this larger gap is likely due to the fact that the algorithms did not yet converge within the 10,000 evaluations as they did for the MaxCoverage problem instances which included the algorithms of exercise 1 experiencing a sharp, sudden improvement before converging. As no sharp improvements were produced for the 10,000 evaluations budget, this could occur in later evaluations with a larger budget.

Additionally for the MaxInfluence problems, the GSEMO algorithm began with and was able to improve further positive fitness values, while within the 10,000 evaluations, none of the RLS, (1+1) EA, and GA were able to achieve non-negative fitness values, improving only by reducing the magnitude of their negative fitness.


# PackWhileTravel Performance

For the PackWhileTravel problem instances, the GSEMO algorithm generally performed the worst compared to the algorithms from exercise 1. The algorithms did not converge for any of the problem instances except for F2300 in which they all converged (GSEMO converging first), for the F2300 problem, GSEMO performed equally to RLS, though worse than (1+1) EA and GA; in the other PackWhileTravelProblems GSEMO was significantly worse than the exercise 1 algorithms in the fitness it achieved.

In most of the PackWhileTravel instances, the GSEMO algorithm initially had a significantly better solutions than the other algorithms, though its improvement from its starting point was minimal and slow, allowing the other algorithms to surpass its performance within the 10,000 evaltuions. However, for problem F2302 GSEMO was significantly worse than the other algorithms for the entireity of the 10,000 evaluations budget, and still suffered from minimal and slow improvement while the algorithms of exercise 1 found significantly larger improvements.


# Summary

The GSEMO algorithm was comprehensively better performing for all of the MaxCoverage and MaxInfluence problem instances, though GSEMO generally performed the worst for the PackWhileTravel problem instances. For the MaxCoverage problems, all algorithms were generally able to converge within the 10,000 evaluations budget; GSEMO converged fastest in all problems MaxCoverage problems. For the MaxInfluence problems, the GSEMO algorithm had an even greater gap of better perforamnce above the algorithms from exercise 1; none of the algorithms converged for the MaxInfluence problems within the 10,000 evaluations budget. The GSEMO algorithm was generally the worst performing algorithm for the PackWhileTravel problems (except for F2300 where it matched RLS), however, it generally started with significantly better solutions at early evaluations compared to the other algorithms, before being surpassed by RLS, (1+1) EA, and GA in later evaluations, with the exception of F2302 where GSEMO was significantly worse for all of the budget.


# First run trade-off plots

The trade-off plots of the first run of GSEMO on the MaxCoverage problem instances have smooth concave curves of the Pareto fronts, indicating that there is a gradual improvement of fitness for the GSEMO algorithm as solution size increases, the concave shape indicates diminishing returns of fitness as solution size increases.

For the MaxInfluence problem instances, the Pareto fronts are generally concave, again indicating diminishing returns for fitness as the solution size increases. The fronts are not smooth, containing small jumps in fitness, this reflects the nature of the problems where disproportionate improvements in fitness can be achieved by adding certain nodes, while others provide little benefit.

For the PackWhileTravel problems, the trade-off front is generally linear, indicating that with increase in solution size, there is consistent fitness improvement, indicating weak conflict between the fitness and size. However, for F2300, the front starts linear though it then plateaus, indicating consistent fitness improvement with weak conflict between fitness and size for small sizes less than 7, though for sizes greater than 7, the plateau suggests diminishing returns of fitness for larger solution sizes.
