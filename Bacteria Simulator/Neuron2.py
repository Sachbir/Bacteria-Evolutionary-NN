class Neuron2:

    def __init__(self, neuron_id, input_structure=None, bias=None):

        self.id = neuron_id

        self.input_structure = input_structure
        self.bias = bias

        self.output = None

    def reset_output(self):
        self.output = None

    def get_output(self):

        if self.output is not None:
            return self.output

        self.output = self.bias
        for neuron in self.input_structure:
            self.output += neuron[0] * neuron[1]

        return self.output


'''
    Neurons' connections are decided by the neural network
    Maybe I should move the random_weight function to 
    NeuralNetwork2 as well. That way all the neuron has to do 
    is what it's told to, and the network decides who connects
    to whom in what way
'''
