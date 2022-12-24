import numpy as np
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator





class NonogramEvaluator(SimpleIndividualEvaluator):

    def __init__(self,
                 clues):  # obligations represents the nonogram headers, the fitness is calculated by the
        self.clues = clues
        super().__init__()


    def _evaluate_individual(self, individual):  # fitness function
        # example:
        # col_clues = [[1, 3], [2], [5], [3], [1]]
        # lower_ob = [[3], [4], [1, 2], [2], [1, 1, 1]]

        # row_clues = self.clues[1]  #todo remove
        # for i, row in enumerate(nonogram):
        #     row_i_clues = row_clues[i]
        #     fitness += self.eval_row_col(row, row_i_clues)

        col_clues = self.clues[0]
        fitness = 0
        nonogram = individual.vector
        for j, column in enumerate(nonogram.T):
            col_i_clues = col_clues[j]
            fitness += self.eval_row_col(column, col_i_clues)

        return fitness

    def pad_with_zeros(self, array1, array2, pad_from_left = False):
        # Find the difference in length between the two arrays
        diff = len(array2) - len(array1)

        if diff > 0:
            padd = (diff, 0) if pad_from_left is True else (0, diff)
            array1 = np.pad(array1, padd, 'constant', constant_values=0)
        elif diff < 0:
            padd = (-diff, 0) if pad_from_left is True else (0, -diff)
            array2 = np.pad(array2, padd, 'constant', constant_values=0)
        return array1, array2

    def eval_row_col(self, row, real_row_clue):
        # row: [1, 0, 0, 1, 0]
        # row_obligation: [1, 2]
        fake_row_clue = self.generate_fake_clue_based_on_row(row)
        return self.eval_by_padding(fake_row_clue, real_row_clue)

    def eval_by_padding(self, fake_row_clue, real_row_clue):
        fake_row_clue_left, real_row_clue_left = self.pad_with_zeros(fake_row_clue, real_row_clue, pad_from_left=True)
        fitness_left = np.sum(np.abs(fake_row_clue_left - real_row_clue_left))

        fake_row_clue_right, real_row_clue_right = self.pad_with_zeros(fake_row_clue, real_row_clue, pad_from_left=False)
        fitness_right = np.sum(np.abs(fake_row_clue_right - real_row_clue_right))

        return min(fitness_left, fitness_right)

    def generate_fake_clue_based_on_row(self, row):
        sequences = []
        i = 0
        while i < len(row):
            # If the current element is a 1, count the number of consecutive 1's
            if row[i] == 1:
                count = 0
                while i < len(row) and row[i] == 1:
                    count += 1
                    i += 1
                sequences.append(count)
            else:
                i += 1
        return np.array(sequences)