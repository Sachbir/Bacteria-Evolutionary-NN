from math import sqrt
import pygame
from random import randrange
from Config import Config
from NeuralNetwork import NeuralNetwork
from WorldObject import WorldObject


class Bacteria(WorldObject):

    color = (0, 0, 0)

    base_size = 4

    def __init__(self, x=0, y=0):

        if x != 0:
            self.x = x
            self.y = y
        else:
            self.x = randrange(Config.world_size[0])
            self.y = randrange(Config.world_size[1])

        self.size = Bacteria.base_size

        self.brain = NeuralNetwork()

        super().__init__(self.x, self.y)

    def update(self, nutrients):

        self.move(nutrients)
        self.eat(nutrients)

        self.render()
        
        return self.reproduce()

    def render(self):

        pygame.draw.circle(WorldObject.screen,
                           Bacteria.color,
                           (int(round(self.x)), int(round(self.y))),
                           self.size,
                           1)

    def get_closest_nutrient(self, nutrients):

        closest_nutrient = (nutrients[0], self.distance_to(nutrients[0]))

        for nutrient in nutrients:
            distance_to_nutrient = self.distance_to(nutrient)
            if distance_to_nutrient > closest_nutrient[1]:
                closest_nutrient = (nutrient, distance_to_nutrient)

        return closest_nutrient[0]

    def move(self, nutrients):

        nutrient = self.get_closest_nutrient(nutrients)

        move_x, move_y = self.brain.get_output((self.x, self.y, nutrient.x, nutrient.y))

        self.x += move_x * Config.move_modifier
        self.y += move_y * Config.move_modifier

        self.x %= Config.world_size[0]
        self.y %= Config.world_size[1]

    def eat(self, nutrients):

        for n in nutrients:
            if n.collides_with(self):
                self.size += 1
                n.destroy()
                break

    def reproduce(self):

        if self.size >= 2 * Bacteria.base_size:
            self.size = Bacteria.base_size
            return True

    def distance_to(self, nutrient):

        delta_x = self.x - nutrient.x
        delta_y = self.y - nutrient.y

        distance_to_point = sqrt(delta_x ** 2 + delta_y ** 2)

        return distance_to_point
