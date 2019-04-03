class Config:

    world_size = 400, 400
    FPS = 60
    background_color = 225, 225, 225
    neuron_weight_variance = 0.25
    input_neuron_count = 4
    output_neuron_count = 2
    move_modifier = 4

    drift_multiplier = 1

    reproduction_requirement = 20


'''
    Input:
        1) Coordinates of self
        2) Coordinates of closest food
    Output:
        1) x speed
        2) y speed
'''
