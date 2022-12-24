import random

from eckity.genetic_operators.genetic_operator import GeneticOperator

class NonogramCrossover(GeneticOperator):
    def __init__(self, probability=1, arity=2, k=2, events=None):
        """
            Vector N Point Mutation.
            Randomly chooses N vector cells and performs a small change in their values.
            Parameters
            ----------
            probability : float
                The probability of the mutation operator to be applied
            arity : int
                The number of individuals this mutation is applied on
            k : int
                Number of points to cut the vector for the crossover.
            events: list of strings
                Events to publish before/after the mutation operator
        """
        self.individuals = None
        self.applied_individuals = None
        self.k = k
        self.points = None
        super().__init__(probability=probability, arity=arity, events=events)

    def apply(self, individuals):
        self.individuals = individuals
        self.points = sorted(random.sample(range(0, len(individuals[0].vector)), self.k))

        start_index = 0
        for end_point in self.points:
            replaced_part = individuals[0].get_vector_part(start_index, end_point)
            replaced_part = individuals[1].replace_vector_row_random(replaced_part, start_index, end_point)
            individuals[0].replace_vector_row_random(replaced_part, start_index, end_point)
            start_index = end_point

        self.applied_individuals = individuals
        return individuals

    def crossover(self, parent1, parent2): ## todo check
        # Choose a random point in the range of the individual size
        crossover_point = random.randint(1, len(parent1) - 1)

        # Create the first offspring by taking the rows from the first parent
        # up to the crossover point, and the rest of the rows from the second parent
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]

        # Create the second offspring by taking the rows from the second parent
        # up to the crossover point, and the rest of the rows from the first parent
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

        return offspring1, offspring2
