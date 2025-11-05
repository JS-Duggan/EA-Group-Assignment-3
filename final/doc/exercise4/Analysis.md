# Performance of the algorithms

The GSEMO algorithm performed comprehensively better than the other algorithms; converging fastest and obtaining the best mean fitness value. On problem F2101, the GSEMO algorithm was marginally beaten in its mean best fitness at 100,000 evaluations, however, GSEMO converged significantly quicker than the other algorithms, and had a significantly wider standard deviation compared to the other algorithms, with significantly better fitness scores than the other algorithms in the range of its wide standard deviation; this suggests that GSEMO was still the best performing algorithm for F2101.

For the MaxCoverage problems, the GSEMO algorithm performed the best. The single-objective closely approximated and performed slightly better than the multi-objective algorithm. For problem F2101, the GA, single-objective EA, and (1+1) EA closely matched the fitness of the GSEMO algorithm at 100,000 evalutations, however, the GA and (1+1) EA took significantly longer to converge; GSEMO had the fastest convergence, and the single-objective and multi-objective EAs, which were matched on convergence speed, were closest of the other algorithms to GSEMO's convergence speed.

For the MaxInfluence problems, the GSEMO algorithm performed the best followed by the single-objective and multi-objective EAs repsectively; these three algorithms performing significantly better than the GA, (1+1) EA, and RLS in both their speed of convergence and achieved fitness.

The GSEMO algorithm was the fastest algorithm to converge across the problems, closely followed by the single-objective and multi-objective EAs, these algorithms had a gradual convergence as evaluations increased; the GA (1+1) EA and RLS took significantly longer to converge, with a staggered improvement of fitness, of these algorithms RLS was consistently the fastest to converge, followed by the (1+1) EA, and GA with slowest convergence among all of the algorithms.


# Improvements achieved in comparison to 10,000 budget results

The 100,000 budget results had the same trend as the 10,000 budget results, the GSEMO algorithm achieved the best performance comprehensively across all problems, however for F2203, the GSEMO algorithm achieved a bigger gap ahead of the single-object EA with a 100,000 budget compared to the 10,000 budget; the other MaxInfluence problems had the single-objective EA close in on the performance GSEMO between the 10,000 budget and 100,000 budget.

Generally for the MaxCoverage problems, the algorithms had already reached a relative convergence by 10,000 evalutations, deriving most improvement within the 10,000 budget and improving only marginally with the remainder of the 100,000 budget; this had the exception of F2103 where the (1+1) EA and GA were able to converge and match the performance of the single-objective EA only within the 100,000 budget. Conversely, for all MaxInfluence problems, all of the algorithms benefitted from the 100,000 budget in comparison to the 10,000 budget, achieving significant improvements beyond 10,000 evaluations.


# GSEMO trade-offs

The trade-off plots for the first run of GSEMO reflect the results where the algorithms improved with a 100,000 budget compared to a 10,000 budget only for the MaxInfluence problems. The trade-off plots with 10,000 budget from exercise 2 compared with the 100,000 budget trade-off plots detail that increasing the budget from 10,000 to 100,000 allowed the algorithm to explore a wider Pareto front only for the MaxInfluence instances, achieving higher objective values and improved coverage of the trade-off space. However, for the MaxCoverage instances the trade-off fronts had no/only marginal difference between the 10,000 and 100,000 budget, indicating that GSEMO had already converged to within the 10,000 evaluation budget.


# Summary
In summary, GSEMO was consistently the best performing algorithm across all problems, the single-objective and multi-objective EAs respectively were generally the next best performing algorithms. The GSEMO algorithm was always the fastest to converge, with single-objective and multi-objective EAs generally matching in convergence speed behind GSEMO, followed by RLS, (1+1) EA, and GA respectively, these with significantly slower convergence. Increasing the budget from 10,000 to 100,000 evalutation improved the performance generally only for the MaxInfluence problems, while the MaxCoverage problems generally did not improve with the increased budget.
