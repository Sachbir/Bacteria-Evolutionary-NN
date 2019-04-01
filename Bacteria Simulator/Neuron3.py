from random import uniform


class Neuron:

    def __init__(self):

        self.neuron_weight_pair = []        # Is that how I want to structure it?
        self.bias = None
        self.depth = None

    @staticmethod
    def get_random_weight():

        return uniform(1, -1)
