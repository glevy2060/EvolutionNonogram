import numpy as np
from eckity.creators.creator import Creator
from eckity.fitness.simple_fitness import SimpleFitness
from NonogramVector import NonogramVector
from itertools import combinations

import random


class NonogramVectorCreator(Creator):
    def __init__(self,
                 length=1,
                 vector_type=NonogramVector,
                 events=None,
                 row_clues=[]):

        if events is None:
            events = ["after_creation"]
        super().__init__(events)

        self.type = vector_type
        self.length = length
        self.row_clues = row_clues

    def create_individuals(self, n_individuals, higher_is_better):
        individuals = [self.type(length=self.length,
                                 fitness= SimpleFitness(higher_is_better= higher_is_better))
                       for _ in range(n_individuals)] ## create n objects of nonogram vector
        for ind in individuals:
            self.create_vector(ind)
        self.created_individuals = individuals
        return individuals

    def create_vector(self, individual):
        nonogram = self.default_gene_creator(individual, self.length) #Todo remove
        nonogram_by_row = self.create_matrix(self.row_clues)
        individual.set_vector(nonogram_by_row)

    def default_gene_creator(self, individual, length):
        return individual.create_nonogram_with_length(length)


    #Todo use this https://towardsdatascience.com/solving-nonograms-with-120-lines-of-code-a7c6e0f627e4
    def choose_row_with_clues(self, row_clue, row_length):
        n_groups = len(row_clue)
        n_empty_left = row_length - (np.sum(row_clue) + len(row_clue) - 1)
        ones = [[1] * x for x in row_clue]
        possibilities = self._create_possibilities(n_empty_left, n_groups, ones)

        # choose randomly from all possibilities
        num_rows = len(possibilities)
        row_index = random.randint(0, num_rows - 1)
        return possibilities[row_index]

    def create_matrix(self, row_clues):
        row_length = len(row_clues)
        matrix = np.zeros((row_length, row_length))
        for i, row_clue in enumerate(row_clues):
            random_row = self.choose_row_with_clues(row_clue, row_length)
            matrix[i] = random_row

        return matrix

    def _create_possibilities(self, n_empty, groups, ones):
        res_opts = []
        for p in combinations(range(groups+n_empty), groups):
            selected = [-1]*(groups+n_empty)
            ones_idx = 0
            for val in p:
                selected[val] = ones_idx
                ones_idx += 1
            res_opt = [ones[val]+[-1] if val > -1 else [-1] for val in selected]
            res_opt = [item for sublist in res_opt for item in sublist][:-1]
            res_opts.append(res_opt)
        return np.asarray(res_opts)