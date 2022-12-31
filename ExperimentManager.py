import matplotlib.pyplot as plt
import numpy as np


class ExperimentManager(object):
    def __init__(self, curr_experiment_num =0, total_num_experiments=0):
        self.total_num_experiment = total_num_experiments
        self.curr_experiment_num = curr_experiment_num
        self.best_fitness_in_all_experiments = 0
        self.best_sol_in_all_experiments = []
        self.num_of_gens_to_reach_best_fitness = 0
        self.best_fitness_over_experiment = []
        self.avg_fitness_over_experiment = []

    def add_experiment_fitness(self, fitness):
        self.best_fitness_over_experiment.append(fitness)

    def add_experiment_avg_fitness(self, avg_fitness):
        self.avg_fitness_over_experiment.append(avg_fitness)

    def plot_best_fitness_over_experiments(self):
        experiment_names = np.arange(1, self.total_num_experiment+1)
        plt.bar(experiment_names, self.best_fitness_over_experiment)
        plt.xlabel('Experiment number')
        plt.ylabel('Best Fitness')
        plt.title('Best Fitness by Experiment')
        plt.show()

    def plot_avg_fitness_over_experiments(self):
        experiment_names = np.arange(1, self.total_num_experiment+1)
        plt.bar(experiment_names, self.best_fitness_over_experiment)
        plt.xlabel('Experiment number')
        plt.ylabel('Avg Fitness')
        plt.title('Avg Fitness by Experiment')
        plt.show()

    def set_best_sol(self, sol_fitness, higher_is_better, sol):
        if higher_is_better and sol_fitness > self.best_fitness_in_all_experiments:
            self.best_fitness_in_all_experiments = sol_fitness
            self.best_sol_in_all_experiments = sol
        if not higher_is_better and sol_fitness < self.best_fitness_in_all_experiments:
            self.best_fitness_in_all_experiments = sol_fitness
            self.best_sol_in_all_experiments = sol

    def plot_best_solution_of_all_experiments(self):
        cmap = plt.get_cmap('binary', 2)
        plt.imshow(self.best_sol_in_all_experiments, cmap=cmap)
        plt.show()
