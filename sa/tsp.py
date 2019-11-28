import random
import numpy as np
import math
import matplotlib.pyplot as plt

from sa.simulated_annealing import SimulatedAnnealing


def plotLearning(sa, nnb, opt_2):
        plt.plot([i for i in range(len(sa.distance_list))], sa.distance_list)
        line_init = plt.axhline(y=sa.initial_distance, color='r', linestyle='--')
        line_min = plt.axhline(y=sa.min_distance, color='g', linestyle='--')
        plt.legend([line_init, line_min], ['Initial distance', 'Optimized distance'])
        plt.ylabel('Distance')
        plt.xlabel('Iteration')
        plt.title("nnb: " + str(nnb) + " and opt_2: " + str(opt_2), loc='center')
        plt.show()

def plotTime(sa, nnb, opt_2):
        list_x = []
        list_y = []
        for x, y in sa.time_temp_list:
            list_x.append(x)
            list_y.append(y)

        plt.scatter(list_x, list_y)
        plt.ylabel('Time')
        plt.xlabel('Temperature')
        plt.title("nnb: " + str(nnb) + " and opt_2: " + str(opt_2), loc='center')
        plt.show()

def node_generate(w_grid, h_grid, num_points):
    xs = np.random.randint(w_grid, size=num_points)
    ys = np.random.randint(h_grid, size=num_points)
    return np.column_stack((xs, ys))

def main():
    n = 25
    temp = math.sqrt(n)
    cooling = 0.95
    stop_temp = 0.01
    stop_iter = 100 * n

    w_grid = 1000
    h_grid = 1000
    num_points = n

    cities = node_generate(w_grid, h_grid, num_points)

    nnb = True
    opt_2 = True
    sa = SimulatedAnnealing(cities, temp, cooling, stop_temp, stop_iter, nnb)
    sa.anneal(opt_2)

    plotLearning(sa, nnb, opt_2)
    plotTime(sa, nnb, opt_2)

if __name__ == "__main__":
    main()
    