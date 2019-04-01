from Config import Config
from Neuron3 import Neuron


class NeuralNetwork:

    def __init__(self):

        self.input_neurons = [Neuron
                              for i in range(Config.input_neuron_count)]
        self.output_neurons = []
        self.neurons = []

    def get_outputs(self, input_values):

        if len(input_values) != len(self.input_neurons):
            raise IndexError('Input count does not match input neuron count')

        for i in range(len(self.input_neurons)):
            neuron = self.input_neurons[i]
            neuron.output_value = input_values[i]

        outputs = []
        for neuron in self.output_neurons:
            outputs.append(neuron.get_output())

        return outputs

    def calc_depth_values(self):

        for neuron in self.output_neurons:
            neuron.depth = 0
            neuron.set_depth_values(0)
