from random import uniform


class Neuron2:

    def __init__(self, input_neurons, template=None):

        self.input_structure = []
        self.bias = None
        self.output = None
        self.depth = 0

        for i in range(len(input_neurons)):
            self.input_structure.append((input_neurons[i],
                                         Neuron2.random_weight()))
        self.bias = Neuron2.random_weight()

    def get_output(self):

        if self.output != 0:
            return self.output

        self.output = self.bias
        for neuron in self.input_structure:
            self.output += neuron[0] * neuron[1]

        return self.output

    @staticmethod
    def random_weight():
        return uniform(-1, 1)
