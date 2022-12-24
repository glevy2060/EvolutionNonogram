from random import randint

from eckity.individual import Individual
import numpy as np


class NonogramVector(Individual):
    def __init__(self,
                 fitness,
                 length=1):
        super().__init__(fitness)

        self.length = length
        self.vector = []

    def create_nonogram_with_length(self, length):
        return np.random.randint(2, size=(length, length))  ##todo think if its good enaugh, how to avoid duplications

    def set_vector(self, vector):
        self.vector = vector
        self.length = len(vector)

    def set_block_distance_vector(self, block_distance_vector):
        self.block_distance_vector = block_distance_vector

    def get_vector(self):
        return self.vector

    def get_vector_part(self, index, end_i):
        # Return vector part from `index` to `end_i'
        return self.vector[index:end_i]

    def replace_vector_row_random(self, inserted_part, start_index, end_index):
        """
        Replace a given vector part in a random position
        Parameters
        -------
        inserted_part: list
            new vector part to be inserted
        Returns
        -------
        list
            previous vector part of this vector genome
        """
        if len(inserted_part) == 0:
            return []

        # Check that the new rows have the same number of columns as the self matrix
        if len(inserted_part[0]) != len(self.vector[0]):
            raise ValueError("New rows must have the same number of columns as the self matrix.")

        # Insert the new rows at the beginning of the self matrix
        # index = randint(0, len(self.vector) - len(inserted_part))  # select a random index
        # end_i = index + len(inserted_part)
        # replaced_part = self.vector[index:end_i]
        # self.vector = np.concatenate((self.vector[:index],inserted_part, self.vector[end_i:]), axis=0)

        # index = randint(0, len(self.vector) - len(inserted_part))  # select a random index
        # end_i = index + len(inserted_part)
        replaced_part = self.vector[start_index:end_index]
        self.vector = np.concatenate((self.vector[:start_index],inserted_part, self.vector[end_index:]), axis=0)
        return replaced_part


    def show(self):
        """
        Print out a simple textual representation of the vector.
        Returns
        -------
        None.
        """
        print(self.vector)


    def execute(self, *args, **kwargs):
        """
        Execute the vector.
        Input is a numpy array or keyword arguments (but not both).
        Parameters
        ----------
        args : arguments
            A numpy array, this is mostly relevant to GP representation.
        kwargs : keyword arguments
            Input to program, this is mostly relevant to GP representation.
        Returns
        -------
        object
            Vector (genome) of this individual.
        """
        return self.get_vector()