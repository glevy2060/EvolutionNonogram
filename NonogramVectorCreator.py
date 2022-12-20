import numpy as np
from eckity.creators.creator import Creator
from eckity.fitness.simple_fitness import SimpleFitness
from NonogramVector import NonogramVector


class NonogramVectorCreator(Creator):
    def __init__(self,
                 length=1,
                 vector_type=NonogramVector,
                 events=None):

        if events is None:
            events = ["after_creation"]
        super().__init__(events)

        self.type = vector_type
        self.length = length

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
        individual.set_vector(nonogram)
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
