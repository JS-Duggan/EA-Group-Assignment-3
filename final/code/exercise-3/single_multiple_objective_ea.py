from ioh import get_problem, ProblemClass
from ioh import logger
import sys
import numpy as np
import random

def bit_flip_mutation(x, prob = 0.01):
    for i in range(len(x)):
        if random.random() < prob:
            x[i] = 1 - x[i]
    return x

def single_objective(fitness, population_size, budget):
    # Initialisation
    # array of size population_size that has an unknown k amount of elements that are included in each individual
    population = [np.random.randint(2, size = fitness.meta_data.n_variables) for _ in range(population_size)]
    #population = [[1 for _ in range(fitness.meta_data.n_variables)] for _ in range(population_size)]

    pop_fitness = [fitness(x) for x in population]
    print(pop_fitness[1])
    best_index = int(np.argmax(pop_fitness))
    best_solution = population[best_index]
    best_fitness = pop_fitness[best_index]

    # Loop
    evaluations = population_size
    while evaluations < budget: # and best_fitness < fitness.optimum.y:


        evaluations += 1

    return best_solution, best_fitness

def run_single_objective():

    fids = [2100, 2101, 2102, 2103, 2200, 2201, 2202, 2203]
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
        for r in range(1):
            res1, res2 = single_objective(prob, 50, 10000)
            if res2 > max:
                max = res2
        print(max)

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
    #run_single_objective()
    om = get_problem(fid = 2100, dimension=50, instance=1, problem_class = ProblemClass.GRAPH)

    fitness = -1
    while fitness <= 0:
        x = np.random.randint(2, size = om.meta_data.n_variables)
        fitness = om(x)
    print(fitness)
