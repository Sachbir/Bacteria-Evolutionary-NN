from Neuron import Neuron


class NeuralNetwork:

    def __init__(self, input_neurons, output_neurons):

        self.input_neurons = []
        self.neurons = []
        self.output_neurons = []

        for i in range(input_neurons):
            self.input_neurons.append(Neuron(1, 0))
        for i in range(output_neurons):
            self.input_neurons.append(Neuron(0, 1))

    def get_output(self, input_values):

        outputs = []
        for neuron in self.output_neurons:
            outputs.append(neuron.get_output(input_values))


''' Idea: Give neurons a value (eg. between 1 and 1000) and neurons can only connect in increasing order, preventing 
loops. Neurons can increase or decrease to accommodate connections if it's a draw, but it might need to be way more 
complicated'''
