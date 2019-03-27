''' Idea: Give neurons a depth value between 0 and 1 in order to randomize the structure of the network'''
''' 
    3 kinds of evolution. In order of likelihood:
        1) Weight tweaks
        2) New connections
        3) New neurons
'''


from Config import Config
from Neuron import Neuron


class NeuralNetwork:

    def __init__(self):

        self.input_neurons = []
        self.neurons = []
        self.output_neurons = []

        for i in range(Config.input_neuron_count):
            self.input_neurons.append(Neuron([], 0))
        for i in range(Config.output_neuron_count):
            self.output_neurons.append(Neuron([], 1, True))

    def get_output(self, input_values):

        for neuron in self.neurons:
            neuron.output = None
        for neuron in self.output_neurons:
            neuron.output = None

        for i in range(len(input_values)):
            self.input_neurons[i].output = input_values[i]

        outputs = []
        for neuron in self.output_neurons:
            outputs.append(neuron.get_output())

        return outputs
