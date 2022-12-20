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
        vector = self.default_gene_creator(individual, self.length)
        individual.set_vector(vector)

    def default_gene_creator(self, individual, length):
        return individual.create_nonogram_with_length(length)
