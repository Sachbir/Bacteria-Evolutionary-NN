import numpy
import random
from Config import Config


class Neuron:

    def __init__(self, input_neurons, depth):

        self.input_neurons = []

        for i in range(len(input_neurons)):
            self.input_neurons.append((input_neurons[i],                # For each neuron
                                       Neuron.get_random_weight()))     # attribute a random weight
        self.bias = Neuron.get_random_weight()                          # and a random bias

        self.depth = depth      # How deep into the network this is (0 = input, 1 = output)

    # Given an array of inputs, return an output
    def get_output(self, input_values):

        if self.depth == 0:
            return          # How do we return the correct input value? Different input neurons have different inputs

        result = self.bias
        for neuron in self.input_neurons:
            neuron_output = neuron[0].get_output(input_values)
            weight = neuron[1]
            result += neuron_output * weight

        return Neuron.modified_sigmoid(result)

    def get_inputs(self):

        return self.input_neurons

    def set_inputs(self, input_neurons, depth, weights, bias, should_vary):

        random_deviance = 0
        if should_vary:
            random_deviance = random.uniform(-Config.neuron_weight_variance, -Config.neuron_weight_variance)
        for i in range(len(input_neurons)):
            self.input_neurons.append((input_neurons[i],                # For each neuron
                                       weights[i] + random_deviance))   # attribute its associated weight
        self.bias = bias + random_deviance                              # and its bias
        self.depth = depth

    @staticmethod
    def get_random_weight():
        return round(random.uniform(-1, 1), 15)

    @staticmethod
    def modified_sigmoid(x):
        return 2 / (1 + numpy.exp(-x)) - 1


'''I think I should add some function to add or remove neurons. At the least, I need to make sure I'm aware of which
neurons are associated with which weights so it's not shifting erratically between generations'''
