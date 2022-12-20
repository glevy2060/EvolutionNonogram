import numpy as np
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator





class NonogramEvaluator(SimpleIndividualEvaluator):

    def __init__(self,
                 obligations):  # obligations represents the nonogram headers, the fitness is calculated by the
        self.obligations = obligations
        super().__init__()


    def _evaluate_individual(self, individual):  # fitness function
        # example:
        # upper_ob = [[1, 3], [2], [5], [3], [1]]
        # lower_ob = [[3], [4], [1, 2], [2], [1, 1, 1]]
        # obligations = np.asarray([upper_ob, lower_ob])

        upper_ob = self.obligations[0]
        left_ob = self.obligations[1]
        total_fitness = 0
        nonogram = individual.vector
        for i, row in enumerate(nonogram):
            left_obligation_of_row_i = left_ob[i]
            total_fitness += self.eval_row_col(row, left_obligation_of_row_i)

        for j, column in enumerate(nonogram.T):
            upper_obligation_of_col_j = upper_ob[j]
            total_fitness += self.eval_row_col(column, upper_obligation_of_col_j)

        return total_fitness

    def pad_with_zeros(self, array1, array2):
        # Find the difference in length between the two arrays
        diff = len(array2) - len(array1)
        if diff > 0:
            array1 = np.pad(array1, (0, diff), 'constant', constant_values=0)
        elif diff < 0:
            array2 = np.pad(array2, (0, -diff), 'constant', constant_values=0)
        return array1, array2

    def eval_row_col(self, row, real_obligation):
        # row: [1, 0, 0, 1, 0]
        # row_obligation: [1, 2]
        fake_obligation = self.create_fake_obligation_from_row(row)
        fake_obligation, real_obligation = self.pad_with_zeros(fake_obligation, real_obligation)
        return np.sum(np.abs(fake_obligation - real_obligation))  # sums the difference between the result row and the real obligation


    def create_fake_obligation_from_row(self, row):
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