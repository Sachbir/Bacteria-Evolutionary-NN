import pygame
from abc import ABC, abstractmethod


class WorldObject(ABC):

    screen = None

    def __init__(self, x, y, *args):

        self.x = x
        self.y = y

        if WorldObject.screen is None:
            WorldObject.screen = pygame.display.get_surface()

    @abstractmethod
    def update(self, *args):
        ...

    @abstractmethod
    def render(self, *args):
        ...
