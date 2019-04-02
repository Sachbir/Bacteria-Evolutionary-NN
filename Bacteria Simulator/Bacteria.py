import pygame
from Config import Config
from copy import deepcopy
from math import sqrt
from NeuralNetwork3 import NeuralNetwork
from Ocean import Ocean
from random import randrange
from WorldObject import WorldObject


class Bacteria(WorldObject):

    color = (0, 0, 0)

    base_size = 4

    def __init__(self, parent=None):

        super().__init__()

        self.x = None
        self.y = None
        self.size = None
        self.collision_box = None
        self.brain = None

        if parent is not None:
            self.x = parent.x
            self.y = parent.y
        else:
            self.x = randrange(Config.world_size[0])
            self.y = randrange(Config.world_size[1])

        self.size = Bacteria.base_size
        self.generate_collision_box()

        self.brain = NeuralNetwork()
        if parent is not None:
            self.set_brain(parent.brain)

    def update(self, nutrients):

        self.move(nutrients)
        self.generate_collision_box()
        self.eat(nutrients)

        super().render(1)
        
        return self.should_reproduce()

    def generate_collision_box(self):

        self.collision_box = pygame.Rect(self.x - self.size,  # left
                                         self.y - self.size,  # top
                                         2 * self.size,       # width
                                         2 * self.size)       # height

    def move(self, nutrients):

        nutrient = self.get_closest_nutrient(nutrients)

        move_x, move_y = self.brain.get_outputs((self.x, self.y, nutrient.x, nutrient.y))

        self.x += move_x * Config.move_modifier
        self.y += move_y * Config.move_modifier

        self.x, self.y = Ocean.drift(self)

    def get_closest_nutrient(self, nutrients):

        closest_nutrient = (nutrients[0], self.distance_to(nutrients[0]))

        for nutrient in nutrients:
            distance_to_nutrient = self.distance_to(nutrient)
            if distance_to_nutrient > closest_nutrient[1]:
                closest_nutrient = (nutrient, distance_to_nutrient)

        return closest_nutrient[0]

    def eat(self, nutrients):

        for n in nutrients:
            if self.collides_with(n):
                self.size += 1
                n.die()
                break

    def should_reproduce(self):

        if self.size >= 2 * Bacteria.base_size:
            self.size = Bacteria.base_size
            return True
        return False

    def distance_to(self, point):

        delta_x = self.x - point.x
        delta_y = self.y - point.y

        distance_to_point = sqrt(delta_x ** 2 + delta_y ** 2)

        return distance_to_point

    def collides_with(self, world_object):

        if self.collision_box.collidepoint(world_object.x, world_object.y):
            return True

    def get_brain(self):
        return self.brain

    def set_brain(self, parent_brain):

        self.brain = deepcopy(parent_brain)

    def multiply(self):

        clone = Bacteria(self.brain)

        self.get_brain().mutate()
        clone.get_brain().mutate()

        return clone
