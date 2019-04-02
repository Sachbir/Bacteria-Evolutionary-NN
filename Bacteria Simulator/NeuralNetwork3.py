from Config import Config
from Neuron3 import Neuron


class NeuralNetwork:

    def __init__(self):

        self.input_neurons = [Neuron()
                              for i in range(Config.input_neuron_count)]
        self.output_neurons = [Neuron()
                               for i in range(Config.output_neuron_count)]
        self.neurons = []

    def get_outputs(self, input_values):

        if len(input_values) != len(self.input_neurons):
            raise IndexError('The number of input values does not match the number of input neurons')

        for i in range(len(self.input_neurons)):
            neuron = self.input_neurons[i]
            neuron.set_output(input_values[i])

        outputs = []
        for neuron in self.output_neurons:
            outputs.append(neuron.get_output())

        return outputs

    def calc_depth_values(self):

        for neuron in self.output_neurons:
            neuron.depth = 0
            neuron.set_depth_values(0)

    def mutate(self):

        # TODO: Add ability for new connections to form (with and without new neurons)

        for neuron in self.output_neurons:
            neuron.mutate()
        for neuron in self.output_neurons:
            neuron.finish_mutating()

        # TODO: Add ability for new connections to form
        #   occasionally create connection with existing neurons
        #   occasionally add a new neuron
