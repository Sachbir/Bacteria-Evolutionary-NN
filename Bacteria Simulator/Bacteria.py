import pygame
import random
from Config import Config
from WorldObject import WorldObject


class Bacteria(WorldObject):

    base_size = 10

    def __init__(self):

        self.size = Bacteria.base_size
        self.color = 0, 0, 0
        self.x = random.randrange(Config.world_size[0])
        self.y = random.randrange(Config.world_size[1])
        self.fullness = 0
        super().__init__(self.x, self.y)

    def update(self, nutrients):

        self.move(random.uniform(-5, 5),
                  random.uniform(-5, 5))
        self.eat(nutrients)

        self.render()

        return self.reproduce()

    def render(self):

        pygame.draw.circle(WorldObject.screen,
                           self.color,
                           (round(self.x), round(self.y)),
                           self.size,
                           1)

    def move(self, delta_x, delta_y):

        right_border = Config.world_size[0]
        bottom_border = Config.world_size[1]

        self.x += delta_x
        self.y += delta_y

        if self.x < 0:
            self.x = 0
        elif self.x > right_border:
            self.x = right_border
        if self.y < 0:
            self.y = 0
        elif self.y > bottom_border:
            self.y = bottom_border

    def eat(self, nutrients):

        for n in nutrients:
            if n.collides_with(self):
                self.size += 1
                n.destroy()
                break

    def reproduce(self):

        if self.fullness >= 2 * Bacteria.base_size:
            return True
