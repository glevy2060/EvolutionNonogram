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
        # obligations = np.asarray([col_clues, lower_ob])

        col_clues = self.clues[0]
        row_clues = self.clues[1]
        fitness = 0
        nonogram = individual.vector
        for i, row in enumerate(nonogram):
            row_i_clues = row_clues[i]
            fitness += self.eval_row_col(row, row_i_clues)

        for j, column in enumerate(nonogram.T):
            col_i_clues = col_clues[j]
            fitness += self.eval_row_col(column, col_i_clues)

        return fitness

    def pad_with_zeros(self, array1, array2):
        # Find the difference in length between the two arrays
        diff = len(array2) - len(array1)
        if diff > 0:
            array1 = np.pad(array1, (0, diff), 'constant', constant_values=0)
        elif diff < 0:
            array2 = np.pad(array2, (0, -diff), 'constant', constant_values=0)
        return array1, array2

    def eval_row_col(self, row, real_row_clue):
        # row: [1, 0, 0, 1, 0]
        # row_obligation: [1, 2]
        fake_row_clue = self.generate_fake_clue_based_on_row(row)
        fake_row_clue, real_row_clue = self.pad_with_zeros(fake_row_clue, real_row_clue)
        return np.sum(np.abs(fake_row_clue - real_row_clue))  # sums the difference between the result row and the real obligation


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