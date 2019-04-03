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

    def modify_self(self):

        # For now we can cheat because all we have are input and output neurons (not connected)

        for neuron in self.input_neurons:
            neuron.modify_self()
        for neuron in self.output_neurons:
            neuron.modify_self()
