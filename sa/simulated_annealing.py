import math
import random
import numpy as np
import time

class SimulatedAnnealing:

    def __init__(self, cities, temp, cooling, stop_temp, stop_iter, nnb):
        """ 
            cities: list - coordinate of cities
            temp: float - t0
            cooling: float - cooling factor
            stop_temp: float - final tp
            stop_iter: int - number iterations
        """
        self.time_temp_list = []
        self.cities = cities
        self.temp = temp
        self.cooling = cooling
        self.stop_temp = stop_temp
        self.stop_iter = stop_iter

        self.sample_size = len(cities)
        self.dist_cities = np.sqrt((np.square(cities[:, np.newaxis] - cities).sum(axis=2)))

        if (nnb):
            self.solution = self.nearestNeighbour(self.dist_cities)
        else:
            self.solution = random.sample(range(len(self.dist_cities)), len(self.dist_cities))

        self.solution_histoty = [self.solution]

        self.actual_distance = self.distance(self.solution)
        self.initial_distance = self.actual_distance
        self.min_distance = self.actual_distance

        self.distance_list = [self.actual_distance]
        print('Initial distance: ', self.actual_distance)

    def nearestNeighbour(self, dist_cities):
        city = random.randrange(len(dist_cities))
        result = [city]

        others_to_visit = list(range(len(dist_cities)))
        others_to_visit.remove(city)

        while others_to_visit:
            nearest_city = min([(dist_cities[city][j], j) for j in others_to_visit], key=lambda x: x[0])
            city = nearest_city[1]
            others_to_visit.remove(city)
            result.append(city)

        return result

    def distance(self, candidate):
        return sum([self.dist_cities[i, j] for i, j in zip(candidate, candidate[1:] + [candidate[0]])])

    def anneal(self, opt_2):
        while self.temp >= self.stop_temp:

            start = time.time()
            
            self.iter = 1
            while self.iter < self.stop_iter:
                candidate = list(self.solution)

                if (opt_2):
                    l = random.randint(2, self.sample_size - 1)
                    i = random.randint(0, self.sample_size - l)
                    candidate[i: (i + l)] = reversed(candidate[i: (i + l)])
                else:
                    random.shuffle(candidate)

                candidate_distance = self.distance(candidate)

                if candidate_distance < self.actual_distance:
                    self.actual_distance = candidate_distance
                    self.solution = candidate
                    if candidate_distance < self.min_distance:
                        self.min_distance = candidate_distance
                        self.best_solution = candidate
                else:
                    if random.random() < math.exp(-abs(candidate_distance - self.actual_distance) / self.temp):
                        self.actual_distance = candidate_distance
                        self.solution = candidate

                self.iter += 1

            end = time.time()
            self.time_temp_list.append((self.temp, (end - start)))

            self.temp *= self.cooling
            self.distance_list.append(self.actual_distance)
            self.solution_histoty.append(self.solution)

            print('Minimum distance: ', self.min_distance)
            print('-- Improvement: ', round((self.initial_distance - self.min_distance) / (self.initial_distance), 4) * 100, '%')

        

    