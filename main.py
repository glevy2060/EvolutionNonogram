import random

from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.subpopulation import Subpopulation

from ExperimentManager import ExperimentManager
from NonogramCrossover import NonogramCrossover
from NonogramVectorCreator import NonogramVectorCreator
from NonogramEvaluator import NonogramEvaluator
import numpy as np

from RunStatistics import RunStatistics

POP_SIZE = 200
MAX_GEN = 200
NUM_EXPERIMENTS = 5
HIGHER_IS_BETTER = True
def main():
    # Initialize the evolutionary algorithm

    # example:
    row_clues = [[3, 3], [2, 4, 2], [1,1], [1,2, 2,1], [1,1,1], [2, 2,2], [1,1], [1,2,1], [2,2], [6]]
    col_clues = [[5], [2, 4], [1, 1, 2], [2, 1, 1], [1, 2, 1, 1], [1,1,1,1,1], [2, 1, 1], [1, 2], [2,4], [5]]

    # col_clues = [[3, 1], [2], [5], [3], [1]] #clues from top to buttom
    # row_clues = [[3], [4], [1, 2], [2], [1, 1, 1]]
    # sol = np.asarray([[ 1.  ,1. , 1., -1., -1.],
    #  [ 1.,  1.,  1.,  1., -1.],
    #  [ 1., -1.,  1.,  1., -1.],
    #  [-1., -1.,  1.,  1., -1.],
    #  [ 1., -1.,  1., -1.,  1.]])
    clues = np.asarray([col_clues, row_clues], dtype=object)
    experiment_manager = ExperimentManager(total_num_experiments = NUM_EXPERIMENTS)
    for EXPERIMENT_COUNT in range(NUM_EXPERIMENTS):
        print(f"\n\n$$$\n\nStarted expirement number {EXPERIMENT_COUNT}\n\n$$$\n\n")
        algo = SimpleEvolution(
            Subpopulation(creators=NonogramVectorCreator(length=len(clues[0]), row_clues= row_clues),
                          population_size=POP_SIZE,
                          evaluator=NonogramEvaluator(clues, higher_is_better=HIGHER_IS_BETTER),
                          higher_is_better=HIGHER_IS_BETTER,
                          elitism_rate=1/300,
                          # genetic operators sequence to be applied in each generation
                          operators_sequence=[
                              NonogramCrossover(probability=0.5, k=1),
                              # NonogramNFlipMutation(probability=0.2, probability_for_each=0.05, n=100)
                          ],
                          selection_methods=[
                              # (selection method, selection probability) tuple
                              (TournamentSelection(tournament_size=3, higher_is_better=HIGHER_IS_BETTER), 1)
                          ]
                          ),
            breeder=SimpleBreeder(),
            max_workers=4,
            max_generation=MAX_GEN,
            # termination_checker=ThresholdFromTargetTerminationChecker(optimal=100, threshold=0.0),
            statistics=RunStatistics(num_generations=MAX_GEN,
                                     higher_is_better=HIGHER_IS_BETTER,
                                     clues =clues,
                                     with_stat_prints=False,
                                     experiment_manager=experiment_manager),
            # We will change the seed to be a new seed in every experiment, since we don't want duplicate results
            random_seed=EXPERIMENT_COUNT
        )

        algo.evolve()

    # Print conclusion over all the experiments
    experiment_manager.plot_best_fitness_over_experiments()
    experiment_manager.plot_avg_fitness_over_experiments()
    experiment_manager.plot_best_solution_of_all_experiments()


if __name__ == '__main__':
    main()
