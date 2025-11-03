# Explination for Single Objective

The single objective function was designed with one point cross over reproduction and gene indepent mutation switching. A low probability was used for each gene flip as individuals would quickly become infeasiable through too many bits being flipped at once. 0.01 to 0.00001 was tested with best results coming from 0.0001 probability. Population generation also uses the same mutation function based on an initial all zero individual, reliying on a higher probability of 0.001 which was optimised to produce a population with high variation and low percentage infeasability. Selection was random based on a probability fitenss/max_fitness. Using the scale relative to 0 instead of the minimum_fitness resulted in a greater variety of indivuiduals selected as the relative scalling would often result in less than 15% of the starting popultion beign kept for reproduction. The best individual was garnteed to be selected for reproduction but was retained outside of the reproduction and mutation process to provide greater chance for gene exploration around this individual in future populations without significantly impacting early exporation over wide areas. The initial cycle was generated before testing was conducted on each stage to the process to determine if it made a significant impact on the results. Chat GPT was used only as a research tool, not in final code implimentation. 


# Explination for Multi Objective

The multi objective funciton was developed with identical reproduction and mutation methods so that the functions could be compared directly based on the selection criteron. The section criteron runs the Pareto algorithm based on minimising size and maximising coverage. It ranks each individual based on wether other individauls in the same or lower ranks dominate it (is weaker than other individuals in all selection criterion). This ranking is then used similar to the single objective function with a 1/rank probability that an individual is selected for the next generation. Given there is not abolute best individual per generation, no individual is directly passed onto the next generation. Chat GPT was used only as a research tool, not in final code implimentation. 


# Analysis of Plots


