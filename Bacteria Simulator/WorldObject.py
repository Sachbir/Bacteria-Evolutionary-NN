import pygame


class WorldObject:

    screen = None
    color = None

    def __init__(self):

        self.x = None
        self.y = None
        self.size = None
        if WorldObject.screen is None:
            WorldObject.screen = pygame.display.get_surface()

    def update(self, *args):
        ...

    def render(self, border=0):

        pygame.draw.circle(self.__class__.screen,
                           self.__class__.color,
                           (int(round(self.x)), int(round(self.y))),
                           self.size,
                           border)
