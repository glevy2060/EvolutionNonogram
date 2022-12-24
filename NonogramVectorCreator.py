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
                                 fitness= SimpleFitness(higher_is_better= higher_is_better)) #todo make sure higher_is_better is correct
                       for _ in range(n_individuals)] ## create n objects of nonogram vector
        for ind in individuals:
            self.create_vector(ind)
        self.created_individuals = individuals
        return individuals

    def create_vector(self, individual):
        nonogram = self.default_gene_creator(individual, self.length)
        block_distance_vector = self.block_distance_creator(nonogram)
        nonogram_by_row = self.create_matrix(self.row_clues)
        individual.set_vector(nonogram_by_row)
        individual.set_block_distance_vector(block_distance_vector)

    def default_gene_creator(self, individual, length):
        return individual.create_nonogram_with_length(length)

    def block_distance_creator(self, nonogram):
        first_block_entries = self.calc_blocks(nonogram)
        distances = []
        for row_blocks in first_block_entries:
            if len(row_blocks) > 0:
                if row_blocks[0] == 0:  # if first block begins from first index
                    distances.append(0)
                else:  # else the distance is the first block index
                    distances.append(row_blocks[0])

            for i in range(0, len(row_blocks)-1):
                curr = row_blocks[i]
                next = row_blocks[i+1]
                distance_between_two_blocks = next - curr - 1
                if distance_between_two_blocks > 1: # example: [1,0,0,0,1] distance_between_two_blocks:3, distance should be 2
                    distance = distance_between_two_blocks - 1
                    distances.append(distance)
                else:
                    distances.append(0)
        return np.asarray(distances)


    def calc_blocks(self, vector):
        first_block_entries = []
        for row in vector:
            is_prev_one = False
            row_blocks = []
            for i, entry in enumerate(row):
                if entry == 1:
                    if not is_prev_one: ##if it's the first 1 in a block
                        row_blocks.append(i)
                        is_prev_one = True
                if entry == 0:
                    is_prev_one = False
            first_block_entries.append(row_blocks)
        return np.asarray(first_block_entries)

    #Todo use this https://towardsdatascience.com/solving-nonograms-with-120-lines-of-code-a7c6e0f627e4
    def choose_row_with_clues(self, row_clue, row_length):
        n_groups = len(row_clue)
        n_empty_left = row_length - (np.sum(row_clue) + len(row_clue) - 1)
        ones = [[1] * x for x in row_clue]
        possibilities = self._create_possibilities(n_empty_left, n_groups, ones)

        # choose randomlly from all possibilities
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