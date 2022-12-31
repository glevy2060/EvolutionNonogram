from sys import stdout
import matplotlib.pyplot as plt
import numpy as np
from eckity.statistics.statistics import Statistics

from ExperimentManager import ExperimentManager


class RunStatistics(Statistics):

    def __init__(self, num_generations,
                 higher_is_better,
                 experiment_manager=ExperimentManager(),
                 clues=[],
                 with_stat_prints=True,
                 format_string=None,
                 output_stream=stdout):
        if format_string is None:
            format_string = 'best fitness {}\nworst fitness {}\naverage fitness {}\n'

        self.num_generations = num_generations
        self.best_fitness_in_gen = []
        self.avg_fitness_in_gen = []
        self.with_stats_prints = with_stat_prints
        self.higher_is_better = higher_is_better
        self.clues = clues
        self.experiment_manager = experiment_manager
        super().__init__(format_string, output_stream)

    def write_statistics(self, sender, data_dict):
        best_fitness_all_gen = 0

        for index, sub_pop in enumerate(data_dict["population"].sub_populations):
            best_individual = sub_pop.get_best_individual()
            best_fitness = best_individual.get_pure_fitness()
            average_fitness = sub_pop.get_average_fitness()
            if self.with_stats_prints:
                print(f'generation #{data_dict["generation_num"]}', file=self.output_stream)
                print(f'subpopulation #{index}', file=self.output_stream)
                print(self.format_string.format(best_fitness,
                                                sub_pop.get_worst_individual().get_pure_fitness(),
                                                average_fitness), file=self.output_stream)

            if self.higher_is_better and best_fitness_all_gen < best_fitness:
                best_fitness_all_gen = best_fitness
            if not self.higher_is_better and best_fitness_all_gen > best_fitness:
                best_fitness_all_gen = best_fitness

            #add params to the graph
            self.best_fitness_in_gen.append(best_fitness)
            self.avg_fitness_in_gen.append(average_fitness)

        if len(self.best_fitness_in_gen) == self.num_generations:
            self.experiment_manager.add_experiment_fitness(best_fitness_all_gen)
            self.experiment_manager.add_experiment_avg_fitness(np.mean(self.avg_fitness_in_gen))
            self.experiment_manager.set_best_sol(best_fitness, self.higher_is_better, sub_pop.get_best_individual().get_vector())
            # self.plot_fitness_over_gen_graph()
            self.print_best_possible_fitness_value()



    # Necessary for valid pickling, since modules cannot be pickled
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['output_stream']
        return state

    # Necessary for valid unpickling, since modules cannot be pickled
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.output_stream = stdout

    def print_best_possible_fitness_value(self):
        if self.higher_is_better: #  count number of col clues
            col_clues = np.array(self.clues[0])
            count = 0
            for row in col_clues:
                count += len(row)
            print(f"Higher_is_better: {self.higher_is_better}\nBest fitness possible: {count}")
        else:
            print(f"Higher_is_better: {self.higher_is_better}\nBest fitness possible: 0")

    def plot_fitness_over_gen_graph(self):
        generations = np.arange(0,self.num_generations)
        plt.plot(generations, self.best_fitness_in_gen, label='Best Fitness')
        plt.plot(generations, self.avg_fitness_in_gen, label='Average Fitness')

        plt.xlabel('Generation')
        plt.ylabel('Fitness Result')
        plt.title('Fitness Results by Generation')
        plt.legend()
        plt.show()