class NeuralNetwork:

    def __init__(self):

        self.input_neurons = []
        self.output_neurons = []
        self.neurons = []

    def get_outputs(self, input_values):

        if len(input_values) != len(input_neurons):
            
