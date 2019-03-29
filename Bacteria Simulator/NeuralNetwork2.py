from Config import Config
from Neuron2 import Neuron2
from random import uniform


class NeuralNetwork:

    def __init__(self):

        self.output_neurons = []
        self.neurons = []           # includes inputs
        self.input_neurons = []

        # Create input -> output
        # Calculate output -> input

    def set_neurons(self, genome=None):

        # Has to be done input-to-output so neurons can find their inputs

        for i in range(Config.input_neuron_count):
            new_neuron = Neuron2()
            self.input_neurons.append(new_neuron)

        # TODO: Figure out the intermediary neurons based on genome

        for i in range(Config.output_neuron_count):
            new_neuron = Neuron2()
            # Figure out neuron connections based on genome
            # As is, it does the default action - gives the output no connections
            self.output_neurons.append(new_neuron)

    def get_output(self, input_values):

        for neuron in self.output_neurons:
            neuron.reset_output()
        for neuron in self.neurons:
            neuron.reset_output()
        for i in range(Config.input_neuron_count):
            self.input_neurons[i].output = input_values[i]

        output_values = []

        for i in range(len(self.output_neurons)):
            output_values[i] = self.output_neurons[i].get_output()

        return output_values

    @staticmethod
    def random_weight():
        return uniform(-1, 1)


'''
    The network is going to read the 'genome', evolve it as it sees fit, and create neurons as such
    Neurons should only be responsible for holding information and acting on it
    
    Genome
        - construct input to output
        - each 'gene' contains id (depth), (id : weight) pairs, and bias
        
        - from each 'gene', a neuron is created and assigned a depth
        - then, that neuron is given another neuron (of a corresponding id) with an associated weight
        - last, it is given a bias
    
    Alternative strategy:
        - do a deep-copy of a neural network
        - use a function to randomize network
            - change values 
'''
# TODO: How to change values if deep-copy
