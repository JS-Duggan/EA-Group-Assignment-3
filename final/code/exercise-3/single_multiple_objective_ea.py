from ioh import get_problem, ProblemClass
from ioh import logger
import numpy as np
import random
import time


def generate_population(population_size, gene_size):
    population = np.zeros((population_size, gene_size), dtype=np.uint8)
    mutation(population, 0.001)
    return population

def selection(population, fitness):

    # Select parents based on 1/n probability scaled based on fitness value
    # There is 0% chance of selecting invalid entires

    fitness_results = np.array(fitness(population), dtype=float)
    max_index = int(np.argmax(fitness_results))
    max_fitness_inverse = 1/fitness_results[max_index]

    # Selects from the population with probbility based on fitness
    # Grantees that the best survives
    return population[np.random.rand(len(population)) < (fitness_results) * max_fitness_inverse], population[max_index]

def selection_multi(population, fitness):

    fitness_results = np.array(fitness(population), dtype=float)

    ranks = np.zeros(len(population), dtype=int)
    unranked = np.arange(len(population), dtype=int)

    rank = 1
    while (unranked.size > 0):
        undominated = []
        for pop in unranked:
            dominated = False
            for pop2 in unranked:
                if (pop == pop2):
                    break
                if (fitness_results[pop2] >  fitness_results[pop] and len(population[pop2]) <= len(population[pop]) or 
                    fitness_results[pop2] >= fitness_results[pop] and len(population[pop2]) <  len(population[pop]) ):
                    dominated = True
                    break
            
            # It is at this rank if it has remained undominated
            if not dominated:
                undominated.append(pop)

        # Update ranks and unranked list
        ranks[undominated] = rank
        rank += 1
        unranked = np.setdiff1d(unranked, undominated)

    # Selection based on probability 1/rank
    return population[np.random.rand(len(population)) < 1/ranks]

def reproduction(parents, population_size):

    # Reproduce through random parent selection, slpit at random point and generate 2 children
    gene_size = len(parents[0])
    parent_size = len(parents)
    population = np.empty((population_size, gene_size), dtype=np.uint8)

    for i in range(0, population_size-1, 2):
        p1 = parents[random.randint(0, parent_size-1)]
        p2 = parents[random.randint(0, parent_size-1)]
        swapIndex = random.randint(0, gene_size-1)
        population[i] = np.concatenate((p1[:swapIndex], p2[swapIndex:]))
        population[i+1] = np.concatenate((p2[:swapIndex], p1[swapIndex:]))

    if population_size % 2 != 0:
        p1 = parents[random.randint(0, parent_size-1)]
        p2 = parents[random.randint(0, parent_size-1)]
        swapIndex = random.randint(0, gene_size-1)
        population[population_size-1] = np.concatenate((p1[:swapIndex], p2[swapIndex:]))

    return population

def mutation(population, prob = 0.001): 
    mask = (np.random.rand(*population.shape) < prob)
    population[mask] = 1-population[mask]

def single_objective(fitness, population_size, budget):
    # Initialisation
    # array of size population_size that has an unknown k amount of elements that are included in each individual
    population = generate_population(population_size, fitness.meta_data.n_variables)

    # Loop
    evaluations = 0
    while evaluations < budget:
        
        # Selection
        parents, max_parent = selection(population, fitness)
        evaluations += len(population)

        # Reproduction
        population = reproduction(parents, population_size-1)
        population = np.vstack([population, max_parent])


        # Mutation
        mutation(population, 0.0001)

    # Find the best combination
    #pop_fitness = [fitness(x) for x in population]
    pop_fitness = fitness(population)
    best_index = int(np.argmax(pop_fitness))
    best_solution = population[best_index]
    best_fitness = pop_fitness[best_index]

    return best_solution, best_fitness

def multi_objective(fitness, population_size, budget):
    # Initialisation
    # array of size population_size that has an unknown k amount of elements that are included in each individual
    population = generate_population(population_size, fitness.meta_data.n_variables)

    # Loop
    evaluations = 0
    while evaluations < budget:
        
        # Selection
        parents = selection_multi(population, fitness)
        evaluations += len(population)

        # Reproduction
        population = reproduction(parents, population_size)

        # Mutation
        mutation(population, 0.0001)

    # Find the best combination
    #pop_fitness = [fitness(x) for x in population]
    pop_fitness = fitness(population)
    best_index = int(np.argmax(pop_fitness))
    best_solution = population[best_index]
    best_fitness = pop_fitness[best_index]

    return best_solution, best_fitness

def run_single_objective():

    fids = [2100, 2101, 2102, 2103, 2200, 2201, 2202, 2203]
    #fids = [2100]
    problems = [
        get_problem(fid=fid, dimension = 50, instance = 1, problem_class = ProblemClass.GRAPH)
        for fid in fids
    ]

    # Create default logger compatible with IOHanalyzer
    # `root` indicates where the output files are stored.
    # `folder_name` is the name of the folder containing all output. You should compress this folder and upload it to IOHanalyzer
    l = logger.Analyzer(root="data", 
        folder_name="run", 
        algorithm_name="Single-Objective EA", 
        algorithm_info="30 instances of monotone submodular probleams with uniform constraint")

    for prob in problems:
        prob.attach_logger(l)
        max = 0
        for r in range(30):
            res1, res2 = single_objective(prob, 50, 10000)
            print(f"Run {r} on F{prob.meta_data.problem_id}: best fitness {res2}")
            if res2 > max:
                max = res2
            prob.reset()
        print("Overall Max: " + str(max))

    # This statemenet is necessary in case data is not flushed yet.
    del l

def run_multi_objective():
    fids = [2100, 2101, 2102, 2103, 2200, 2201, 2202, 2203]
    #fids = [2203]
    problems = [
        get_problem(fid=fid, dimension = 50, instance = 1, problem_class = ProblemClass.GRAPH)
        for fid in fids
    ]

    # Create default logger compatible with IOHanalyzer
    # `root` indicates where the output files are stored.
    # `folder_name` is the name of the folder containing all output. You should compress this folder and upload it to IOHanalyzer
    l = logger.Analyzer(root="data", 
        folder_name="run", 
        algorithm_name="Multi-Objective EA", 
        algorithm_info="30 instances of monotone submodular probleams with uniform constraint")

    for prob in problems:
        prob.attach_logger(l)
        max = 0
        for r in range(30):
            res1, res2 = multi_objective(prob, 50, 10000)
            print(f"Run {r} on F{prob.meta_data.problem_id}: best fitness {res2}")
            if res2 > max:
                max = res2
            prob.reset()
        print("Overall Max: " + str(max))

    # This statemenet is necessary in case data is not flushed yet.
    del l

if __name__ == "__main__":
    run_multi_objective()
    
