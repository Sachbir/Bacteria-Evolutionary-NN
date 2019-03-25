from Neuron import Neuron


class NeuralNetwork:

    def __init__(self, input_neurons, output_neurons):

        self.input_neurons = []
        self.neurons = []
        self.output_neurons = []

        for i in range(input_neurons):
            self.input_neurons.append(Neuron([], 0))
        for i in range(output_neurons):
            self.input_neurons.append(Neuron([], 1))

    def get_output(self, input_values):

        for neuron in self.neurons:
            neuron.output = None
        for neuron in self.output_neurons:
            neuron.output = None

        for i in range(input_values):
            self.input_neurons[i].output = input_values[i]

        outputs = []
        for neuron in self.output_neurons:
            outputs.append(neuron.get_output())


''' Idea: Give neurons a depth value between 0 and 1 in order to randomize the structure of the network'''
''' 
    3 kinds of evolution. In order of likelihood:
        1) Weight tweaks
        2) New connections
        3) New neurons
'''
