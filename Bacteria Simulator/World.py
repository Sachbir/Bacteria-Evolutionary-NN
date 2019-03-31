import pygame
import sys
from Bacteria import Bacteria
from Config import Config
from Nutrient import Nutrient


class World:

    pygame.init()
    screen = pygame.display.set_mode(Config.world_size)
    clock = pygame.time.Clock()

    def __init__(self):

        self.pause = False

        print("\n---INITIALIZE---\n")

    def run(self):

        bacteria = [Bacteria()]
        nutrients = [Nutrient()
                     for i in range(100)]

        while True:
            if not self.pause:
                self.process_events()

                World.screen.fill(Config.background_color)  # Off-white

                for i in range(len(bacteria) - 1, -1, -1):
                    full = bacteria[i].update(nutrients)
                    if full:
                        bacteria.append(Bacteria(bacteria[i]))
                        bacteria.append(Bacteria(bacteria[i]))
                        del bacteria[i]

                for n in nutrients:
                    n.update()

            pygame.display.flip()
            World.clock.tick(Config.FPS)

    def process_events(self):

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_q)):  # End simulation
                print("\n------QUIT------")
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.pause = True


world = World()
world.run()