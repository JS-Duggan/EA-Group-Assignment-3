# Explination for Single Objective

The single objective function was designed with one point cross over reproduction and gene indepent mutation switching. A low probability was used for each gene flip as individuals would quickly become infeasiable through too many bits being flipped at once. 0.01 to 0.00001 was tested with best results coming from 0.0001 probability. Population generation also uses the same mutation function based on an initial all zero individual, reliying on a higher probability of 0.001 which was optimised to produce a population with high variation and low percentage infeasability. Selection was random based on a probability fitenss/max_fitness. Using the scale relative to 0 instead of the minimum_fitness resulted in a greater variety of indivuiduals selected as the relative scalling would often result in less than 15% of the starting popultion beign kept for reproduction. The best individual was garnteed to be selected for reproduction but was retained outside of the reproduction and mutation process to provide greater chance for gene exploration around this individual in future populations without significantly impacting early exporation over wide areas. The initial cycle was generated before testing was conducted on each stage to the process to determine if it made a significant impact on the results. Chat GPT was used only as a research tool, not in final code implimentation. 


# Explination for Multi Objective

The multi objective funciton was developed with identical reproduction and mutation methods so that the functions could be compared directly based on the selection criteron. The section criteron runs the Pareto algorithm based on minimising size and maximising coverage. It ranks each individual based on wether other individauls in the same or lower ranks dominate it (is weaker than other individuals in all selection criterion). This ranking is then used similar to the single objective function with a 1/rank probability that an individual is selected for the next generation. Given there is not abolute best individual per generation, no individual is directly passed onto the next generation. Chat GPT was used only as a research tool, not in final code implimentation. 


# Analysis of Plots
A description of the single-, multi-objective EA's, and the GSEMO algorithm is provided for each of the problem instances. Note, the graphs have a logarithmic scale for the x-axis (the number of function evaluations). The mean and standard deviations for each graph were also enabled, providing a visual representation of the variance 

## f2100:
The single- and multi-objective EA reached a best so far value of 420.87 and 410.1 respecitvely and the GSEMO aglorithm reached a higher value of 443. The single- and multi-objective EA's had a similar steady increase to their respective maximum values, while the GSEMO had a much more rapid increase until it reached a varue of around 400 before exhibiting a steady increase. Additionally, GSEMO had large variability during its earliest phase and exhibited a tighter variance during later evaluations, particular around the 100 evaluations mark. On the other hand, the single- and multi-objective EA's had a moderate variance throughout, only becoming smaller around the 1000 evaluations mark. While all 3 algorithms had diminishing returns as the number of evaluations increased, GSEMO kept adding small gains to reach a higher f(x) value, while the other two algorithsm plateaued. 

## f2101:
Similar to the f2100 problem instance, GSEMO out performed single- and multi-objective, this time reaching a value of 442.33, followed by single-objective at 421.33, and finally multi-objective reached an f(x) value of 408.13. Another difference for this problem instance is that GSEMO had little to no variance around the 5 function evaluations mark, then exhibited moderate variance until just before the 100 evaluation mark. Single- and multi-objective had an initial high variance, which steadily decreased as their f(x) values plateaued.

## f2102:
GSEMO reached a mximum f(x) value of 561.39 while single- and multi-objective reached 533.67 and 516.9 respectively. In this instance, GSEMO went from large to small variance, straying away from its usual strict behaviour at higher evaluations. Single- and multi-objective EA's followed their usual trend of a steadily decrease variance. 

## f2103:
GSEMO reached a mximum f(x) value of 710 while single- and multi-objective reached 668.57 and 641.87 respectively. In this instance, all 3 algorithms followed their usual variance trends, with GSEMO exhibiting high varaibility at earlier evaluations, which drastically became stricter at higher evaluations. 

## f2200:
All 3 algorithms exhibited a steady increase throughout; GSEMO reached a maximum value of 585.9, while single- and multi-objective reached 388.81 and 238.7 respectively. Hence, the MaximumInfluence instances showed a larger difference in maximum f(x) values between all 3 algorithms, however, it still follwed the general trend of GSEMO > single-objective > multi-objective. Conversely to the MaximumCoverage instances, the shaded region for the 3 algorithms at lower evaluations was small, and then the spread increased as the evaluations increased. This indicates that the variance of the 3 algorithms increased with evaluations, opposite to the decreasing variance trend observed with MaximumCoverage.

## f2201:
GSEMO reached a mximum f(x) value of 731.39 while single- and multi-objective reached 491.71 and 331.48 respectively. In this instance, all 3 algorithms followed their usual variance trends, with GSEMO exhibiting low varaibility at earlier evaluations, which drastically became larger at higher evaluations. 

## f2202:
GSEMO reached a mximum f(x) value of 907.14 while single- and multi-objective reached 737.72 and 620.22 respectively. In this instance, all 3 algorithms followed their usual variance trends.

## f2203:
This instance did not follow any of the usual trends. Mutli-objective achieved the highest result at 970.19, while single-objective and GSEMO reached 964.35 and 954.85 respectively. The variance for all 3 algorithms was more of a steady increase and remained relatively consistent throughout as the function evaluations increased. 

Across the MaxCoverage and MaxInfluence problem instances, a general and consistent trend was observed in the maximum achieved f(x) value: GSEMO > single-objective > multi-objective. This trend was only broken in the f2203 instance, where the order reversed. This is expected as GSEMO prevents early convergence, attritubuting to its faster rise. The single-obejective EA generally shows a more gradual increase and plateaus early once diversty decreases, while multi-objective shows a similar behaviour, performing slightly worse than its single-objective couterpart. 

For MaxCoverage problem instances, variance decreased over time, indicating solutions became more stable. On the other hand, MaxInfluence instances showed an increasing variance, indicating more of an exploratory approach. The outlying instance was f2203, where multi-objective performed the best. This shows that maintaining broader trade-offs earlier in the search can sometimes be more effective than just aggressively maximising marginal gain like GSEMO. However, the results overall show that GSEMO performed the best across all MaxCoverage and MaxInfluence problem instances, showing that it can be a robust baseline for monotone submodular optimsation. 




