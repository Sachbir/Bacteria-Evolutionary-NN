from random import uniform


class Neuron:

    def __init__(self):

        self.neuron_weight_pair = []        # Is that how I want to structure it?
        self.bias = None
        self.depth = None
        self.output_value = None

    def get_output(self):

        if self.output_value:
            return self.output_value

    def set_depth_values(self, depth_of_caller):

        for i in range(len(self.neuron_weight_pair)):
            depth = depth_of_caller + 1
            if depth < self.depth:
                return
            neuron = self.neuron_weight_pair[i][0]
            neuron.set_depth_values(self.depth)

    #TODO: Check if this is good
    def reset_depth_value(self):

        self.depth = 0
        for i in range(len(self.neuron_weight_pair)):
            neuron = self.neuron_weight_pair[i][0]
            neuron.reset_depth_value()

    @staticmethod
    def get_random_weight():

        return uniform(1, -1)
