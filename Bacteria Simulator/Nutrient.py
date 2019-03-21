import pygame
import random
from Config import Config
from WorldObject import WorldObject


class Nutrient(WorldObject):

    radius = 30

    def __init__(self):

        self.color = 0, 0, 0
        self.x = random.randrange(Config.world_size[0])
        self.y = random.randrange(Config.world_size[1])
        self.collision_box = None
        self.dead = False

        self.generate_collision_box()

        super().__init__(self.x, self.y)

    def update(self):

        if not self.dead:
            self.render()

    def render(self):

        pygame.draw.circle(WorldObject.screen,
                           self.color,
                           (self.x, self.y),
                           Nutrient.radius)

    def generate_collision_box(self):

        if self.dead:
            self.collision_box = pygame.Rect(0, 0, 0, 0)  # height
            return
        self.collision_box = pygame.Rect(self.x - 2 * Nutrient.radius,  # left
                                         self.y - 2 * Nutrient.radius,  # top
                                         4 * Nutrient.radius,       # width
                                         4 * Nutrient.radius, )     # height

    def collides_with(self, world_object):

        if self.collision_box.collidepoint(world_object.x, world_object.y):
            return True

    def destroy(self):

        self.dead = True
        self.generate_collision_box()
