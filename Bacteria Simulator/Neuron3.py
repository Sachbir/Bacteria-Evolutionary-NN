from Config import Config
from numpy import exp
from random import uniform


class Neuron:

    def __init__(self):

        self.neuron_weight_pair = []    # Contains an input neuron, and how strongly its input should be factored in
        self.bias = Neuron.get_random_weight()
        self.depth = None               # When should this be calculated?
        self.output_value = None
        self.has_mutated = False

    def add_input_neuron(self, neuron):
        self.neuron_weight_pair.append([neuron,
                                        Neuron.get_random_weight()])

    # If the output value already calculated, skip the calculation
    # Return the output value
    def get_output(self):

        if self.output_value is not None:
            return self.output_value

        self.output_value = self.bias
        for neuron_weight_pair in self.neuron_weight_pair:
            input_neuron = neuron_weight_pair[0]
            weight = neuron_weight_pair[1]
            self.output_value += input_neuron.output_value * weight
        self.output_value = Neuron.modified_sigmoid(self.output_value)
        return self.output_value

    def set_output(self, output_value):
        self.output_value = output_value

    # Determine how far from the output neuron a given neuron is
    # If a depth value was previously set, the neuron takes the largest value
    # This is used for constructing valid networks
    #   This is to avoid loops
    def set_depth_values(self, depth_of_caller):

        for i in range(len(self.neuron_weight_pair)):
            depth = depth_of_caller + 1
            if depth <= self.depth:
                return
            neuron = self.neuron_weight_pair[i][0]
            neuron.set_depth_values(self.depth)

    def mutate(self):

        if self.has_mutated:
            return

        for neuron_weight_pair in self.neuron_weight_pair:
            neuron_weight_pair[0].mutate()

            random_deviation = uniform(-Config.neuron_weight_variance, Config.neuron_weight_variance)
            neuron_weight_pair[1] += random_deviation
        random_deviation = uniform(-Config.neuron_weight_variance, Config.neuron_weight_variance)
        self.bias += random_deviation

        self.has_mutated = True

    def finish_mutating(self):

        if self.has_mutated is False:
            return

        for neuron_weight_pair in self.neuron_weight_pair:
            neuron_weight_pair[0].finish_mutating()

        self.has_mutated = False

    # This is called to remove all depth values before recalculating them
    # TODO: Can this be factored into the set_depth_value function?
    def reset_depth_value(self):

        self.depth = None
        for i in range(len(self.neuron_weight_pair)):
            neuron = self.neuron_weight_pair[i][0]
            neuron.reset_depth_value()

    @staticmethod
    def get_random_weight():
        return uniform(1, -1)

    @staticmethod
    def modified_sigmoid(x):
        return 2 / (1 + exp(-x)) - 1
