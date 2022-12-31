from eckity.genetic_operators.failable_operator import FailableOperator
from random import sample


class NonogramNFlipMutation(FailableOperator):
    def __init__(self, n=1, probability=1, arity=1, mut_val_getter=None,
                 success_checker=None, events=None, attempts=5):
        super().__init__(probability=probability, arity=arity, events=events, attempts=attempts)
        self.n = n

        if success_checker is None:
            success_checker = self.default_success_checker
        self.success_checker = success_checker

        if mut_val_getter is None:
            mut_val_getter = self.default_mut_val_getter
        self.mut_val_getter = mut_val_getter

    def on_fail(self, payload):
        pass

    def attempt_operator(self, individuals, attempt_num):
        succeeded = True
        for individual in individuals:
            old_individual = individual.clone()

            # randomly select n points of the vector (without repetitions)
            m_points = sample(range(individual.size()), k=self.n)
            # obtain the mutated values
            mut_vals = [self.mut_val_getter(individual, m_point) for m_point in m_points]

            # update the mutated value in-place
            for m_point, mut_val in zip(m_points, mut_vals):
                individual.set_cell_value(m_point, mut_val)

            if not self.success_checker(old_individual, individual):
                succeeded = False
                individual.set_vector(old_individual.vector)
                break

        self.applied_individuals = individuals
        return succeeded, individuals

    @staticmethod
    def default_mut_val_getter(nonogram, idx):
        return 1 #Todo change to random
