from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.subpopulation import Subpopulation

from NonogramCrossover import NonogramCrossover
from NonogramVectorCreator import NonogramVectorCreator
from NonogramEvaluator import NonogramEvaluator
import numpy as np


def main():
    # Initialize the evolutionary algorithm

    # example:
    upper_ob = [[1, 3], [2], [5], [3], [1]]
    lower_ob = [[3], [4], [1, 2], [2], [1, 1, 1]]
    clues = np.asarray([upper_ob, lower_ob], dtype=object)
    population_size = 300
    algo = SimpleEvolution(
        Subpopulation(creators=NonogramVectorCreator(length=len(clues[0])),
                      population_size=population_size,
                      evaluator=NonogramEvaluator(clues),
                      higher_is_better=False,
                      elitism_rate=1/300,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          NonogramCrossover(probability=0.5, k=1),
                          # BitStringVectorNFlipMutation(probability=0.2, probability_for_each=0.05, n=100)
                      ],
                      selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=3, higher_is_better=False), 1)
                      ]
                      ),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=4,
        # population_evaluator=
        # termination_checker=ThresholdFromTargetTerminationChecker(optimal=100, threshold=0.0),
        # statistics=BestAverageWorstStatistics()
    )

    # evolve the generated initial population
    algo.evolve()

    # Execute (show) the best solution
    print(algo.execute())


if __name__ == '__main__':
    main()
