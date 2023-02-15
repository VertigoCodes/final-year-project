import random
import numpy as np

def create_distance_matrix(locations):
    num_locs = len(locations)
    dist_mat = np.zeros((num_locs, num_locs))
    for i in range(num_locs):
        for j in range(num_locs):
            dist_mat[i][j] = np.sqrt((locations[i][0]-locations[j][0])**2 + (locations[i][1]-locations[j][1])**2)
    return dist_mat

def create_population(size, num_locs):
    population = []
    for i in range(size):
        individual = list(range(num_locs))
        random.shuffle(individual)
        population.append(individual)
    return population

def evaluate_fitness(individual, distance_matrix):
    dist = 0
    for i in range(len(individual)):
        j = (i + 1) % len(individual)
        dist += distance_matrix[individual[i]][individual[j]]
    return 1/dist

def select_parents(population, distances):
    fitnesses = [evaluate_fitness(individual, distances) for individual in population]
    sum_fitnesses = sum(fitnesses)
    probabilities = [fitness/sum_fitnesses for fitness in fitnesses]
    parent1, parent2 = random.choices(population, weights=probabilities, k=2)
    return parent1, parent2

def breed(parent1, parent2):
    child = [None] * len(parent1)
    gene_a, gene_b = random.sample(range(len(parent1)), 2)
    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    for i in range(start_gene, end_gene + 1):
        child[i] = parent1[i]

    remaining = [item for item in parent2 if item not in child]
    for i in range(len(child)):
        if child[i] is None:
            child[i] = remaining.pop(0)

    return child

def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))
            city1 = individual[swapped]
            city2 = individual[swap_with]
            individual[swapped] = city2
            individual[swap_with] = city1
    return individual

def evolve_population(population, distances, mutation_rate, elitism_rate):
    num_elites = int(len(population) * elitism_rate)
    elites = sorted(population, key=lambda x: evaluate_fitness(x, distances), reverse=True)[:num_elites]
    offspring = []

    while len(offspring) < len(population) - num_elites:
        parent1, parent2 = select_parents(population, distances)
        child = breed(parent1, parent2)
        offspring.append(mutate(child, mutation_rate))

    population = elites + offspring
    return population

def tsp_genetic_algorithm(locations, pop_size=100, elitism_rate=0.1, mutation_rate=0.01, num_generations=100):
    num_locs = len(locations)
    distances = create_distance_matrix(locations)
    population = create_population(pop_size, num_locs)
    best_individual = None
    best_fitness = -1

    for generation in range(num_generations):
        population = evolve_population(population, distances, mutation_rate, elitism_rate)
        current_best = max(population, key=lambda x: evaluate_fitness(x, distances))
        current_fitness = evaluate_fitness(current_best, distances)

        if current_fitness > best_fitness:
            best_individual = current_best
