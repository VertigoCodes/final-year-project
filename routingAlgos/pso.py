import random
import numpy as np

# Define TSP problem data
distance_matrix = np.array([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
num_cities = distance_matrix.shape[0]

# Define PSO parameters
num_particles = 10
max_iterations = 100
c1 = 1.5
c2 = 1.5
w = 0.7

# Define particle class
class Particle:
    def __init__(self, position):
        self.position = position
        self.velocity = np.zeros(num_cities)
        self.best_position = position
        self.best_fitness = float('inf')
        self.fitness = self.evaluate_fitness()
        
    def evaluate_fitness(self):
        # Calculate the total distance for the current tour
        dist = 0
        for i in range(num_cities-1):
            dist += distance_matrix[self.position[i], self.position[i+1]]
        dist += distance_matrix[self.position[-1], self.position[0]]
        return dist
    
    def update_velocity(self, global_best_position):
        r1 = np.random.rand(num_cities)
        r2 = np.random.rand(num_cities)
        self.velocity = w*self.velocity + c1*r1*(self.best_position - self.position) + c2*r2*(global_best_position - self.position)
        
    def update_position(self):
        self.position = np.roll(self.position, np.argmax(self.velocity))
        self.fitness = self.evaluate_fitness()
        
        # Update best position if current position is better
        if self.fitness < self.best_fitness:
            self.best_position = self.position
            self.best_fitness = self.fitness

# Define PSO algorithm
class PSO:
    def __init__(self):
        self.swarm = [Particle(np.random.permutation(num_cities)) for i in range(num_particles)]
        self.global_best_position = self.swarm[0].position
        self.global_best_fitness = float('inf')
        
    def optimize(self):
        for i in range(max_iterations):
            # Update global best position
            for particle in self.swarm:
                if particle.best_fitness < self.global_best_fitness:
                    self.global_best_position = particle.best_position
                    self.global_best_fitness = particle.best_fitness
            
            # Update particle velocities and positions
            for particle in self.swarm:
                particle.update_velocity(self.global_best_position)
                particle.update_position()
            
            print('Iteration:', i+1, 'Best fitness:', self.global_best_fitness, 'Best tour:', self.global_best_position)
            
# Run PSO algorithm
pso = PSO()
pso.optimize()
