from ioh import get_problem, ProblemClass
from ioh import logger
import sys
import numpy as np
import random
import math



def bit_flip_mutation(x, prob = 0.01):
    for i in range(len(x)):
        if random.random() < prob:
            x[i] = 1 - x[i]
    return x

def generate_population(population_size, gene_size, fitness):
    population = [[0 for _ in range(gene_size)] for _ in range(population_size)]

    for pop in population:
        # Generate only genes that have valid results
        res = 0
        temp = pop
        while (res <= 0):
            temp = bit_flip_mutation(pop, 0.001)
            res = fitness(temp)
        pop = temp

    return population

def selection(population, fitness):

    # Select parents based on 1/n probability scaled based on fitness value
    # There is 0% chance of selecting invalid entires

    fitness_results = [fitness(x) for x in population]
    max_index = int(np.argmax(fitness_results))
    max_fitness = fitness_results[max_index]

    # Grantee that the best survives
    new_population = [(population[max_index])]

    #print("test")
    #print(len(new_population))
    #print(len(new_population[0]))

    for i in range(len(population)):
        if (random.random() < fitness_results[i] / max_fitness):
            new_population.append(population[i])

    return new_population

def reproduction(parents, population_size):

    # Reproduce through random parent selection, slpit at random point and generate 2 children

    population = []
    gene_size = len(parents[0])
    parent_size = len(parents)

    for _ in range(math.floor(population_size/2)):
        p1 = parents[random.randint(0, parent_size-1)]
        p2 = parents[random.randint(0, parent_size-1)]
        swapIndex = random.randint(0, gene_size-1)
        population.append( p1[:swapIndex] + p2[swapIndex:])
        population.append( p2[:swapIndex] + p1[swapIndex:])

    # Add the best to stay around
    # assumes the first parent is the best, keep this
    if population_size % 2 == 0:
        # Even popultion which is filled above, replace the first one
        population[0] = parents[0] 
    else:
        # Odd population so append the last required population to be the best
        population.insert(0, parents[0])
    return population

def mutation(population): 
    # Run bit flipping on all population
    # Keep the best untouched
    result = [bit_flip_mutation(pop, 0.001) for pop in population[1:]]
    result.append(population[0])
    return result

def single_objective(fitness, population_size, budget):
    # Initialisation
    # array of size population_size that has an unknown k amount of elements that are included in each individual
    population = generate_population(population_size, fitness.meta_data.n_variables, fitness)
    #[np.random.randint(2, size = fitness.meta_data.n_variables) for _ in range(population_size)]

    # Loop
    evaluations = 0
    while evaluations < budget:
        
        # Selection
        parents = selection(population, fitness)
        evaluations += len(population)

        # Reproduction
        population = reproduction(parents, population_size)

        # Mutation
        population = mutation(population)
        #print("Test 1")
        #print(len(population))
        #print(len(population[0]))


    pop_fitness = [fitness(x) for x in population]
    best_index = int(np.argmax(pop_fitness))
    best_solution = population[best_index]
    best_fitness = pop_fitness[best_index]

    return best_solution, best_fitness

def run_single_objective():

    """"
    fids = [2100, 2101, 2102, 2103, 2200, 2201, 2202, 2203]"""
    fids = [2203]
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
        for r in range(10):
            res1, res2 = single_objective(prob, 51, 10000)
            print(f"Run {r} on F{prob.meta_data.problem_id}: best fitness {res2}")
            if res2 > max:
                max = res2
        print("Overall Max: " + str(max))

    # This statemenet is necessary in case data is not flushed yet.
    del l

def run_multi_objective():
    # Create default logger compatible with IOHanalyzer
    # `root` indicates where the output files are stored.
    # `folder_name` is the name of the folder containing all output. You should compress this folder and upload it to IOHanalyzer
    l = logger.Analyzer(root="data", 
        folder_name="run", 
        algorithm_name="Single-Objective EA", 
        algorithm_info="30 instances of monotone submodular probleams with uniform constraint")

    om = get_problem(fid = 2100, problem_class = ProblemClass.GRAPH)

    om.attach_logger(l)
    print (om.meta_data.n_variables)


    # This statemenet is necessary in case data is not flushed yet.
    del l
    return 1

if __name__ == "__main__":
    run_single_objective()
    
    
    """om = get_problem(fid = 2100, dimension=50, instance=1, problem_class = ProblemClass.GRAPH)

    data = [0 for _ in range(om.meta_data.n_variables)]
    data[0] = 1
    print(om(data))

    fitness = -1
    while fitness <= 0:
        x = np.random.randint(2, size = om.meta_data.n_variables)
        fitness = om(x)
    print(fitness)"""
