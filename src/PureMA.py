from create_problem_sets import parameters
from Genetic import genetic_algorithem


class PureMA(genetic_algorithem):
    def __init__(self, target, tar_size, pop_size, problem_spec, fitnesstype, selection):
        genetic_algorithem.__init__(self, target, tar_size, pop_size, problem_spec, 0, fitnesstype, selection,
                                    0, 0, 0, 0)

    def algo(self, i):
        self.calc_fitness()  # evaluate all individuals in population
        self.evolve()  # evolve a new population
        self.select_improve()  # select individuals to be improved and work on them

    def stopage(self, i):
        k = i == 1000
        # todo: add another condition for complition
        other_condition = True
        return k and other_condition

    def evolve(self):
        # todo: evolve a new population !
        pass
    def select_improve(self):
        # todo: select subset of individuals put them in selected
        selected = self.selection()
        # todo: individual improvment
        # todo: perform learning using meems for every individual in selected
        self.learning(selected)
        # todo: continue with Lemarkian or Baldwin learning
        self.lem_bald_learning(selected)

    def selection(self):
        selected = []
        # todo: from population select individuals
        return selected

    def learning(self, sub_population):
        # learn using memes
        pass

    def lem_bald_learning(self, sub_population, type_of_learning):
        return self.baldwin(sub_population) if type_of_learning else self.lemarckian()

    def baldwin(self, sub_population):
        pass

    def lemarckian(self, sub_population):
        pass
