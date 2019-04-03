import pygame
import sys
from time import time
from Bacteria import Bacteria
from Config import Config
from Nutrient import Nutrient


class World:

    pygame.init()
    screen = pygame.display.set_mode(Config.world_size)
    clock = pygame.time.Clock()

    def __init__(self):

        self.pause = False
        self.effective_FPS = None
        self.bacteria = None
        self.nutrients = None

        print("\n---INITIALIZE---\n")

    # noinspection PyUnusedLocal
    def run(self):

        self.bacteria = [Bacteria()]
        self.nutrients = [Nutrient()
                          for i in range(1000)]

        while True:
            start_time = time()

            self.process_events()
            if not self.pause:

                World.screen.fill(Config.background_color)  # Off-white

                for i in range(len(self.bacteria) - 1, -1, -1):
                    this_bacteria = self.bacteria[i]
                    full = this_bacteria.update(self.nutrients)
                    if full:
                        self.bacteria.append(this_bacteria.multiply())

                for n in self.nutrients:
                    n.update()

            pygame.display.flip()
            World.clock.tick(Config.FPS)

            end_time = time()

            effective_FPS = int(round(1 / (end_time - start_time), -1))
            if self.effective_FPS != effective_FPS:
                self.effective_FPS = effective_FPS

    def process_events(self):

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_q)):  # End simulation
                print("\n------QUIT------")
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.toggle_pause()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                Config.FPS += 10
                print("Target FPS: " + str(Config.FPS))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if Config.FPS == 10:
                    Config.FPS = 0
                elif Config.FPS > 0:
                    Config.FPS -= 10
                print("Target FPS: " + str(Config.FPS))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:    # Information
                print("\n------INFO------")
                print("Effective FPS: " + str(self.effective_FPS))
                print("Bacteria: " + str(len(self.bacteria)))
                print("Nutrients: " + str(len(self.nutrients)))
                print("----------------\n")

    def toggle_pause(self, setting=None):

        if setting is None:
            self.pause = not self.pause
        else:
            self.pause = setting

        if self.pause:
            print("Paused")
        else:
            print("Resumed")



world = World()
world.run()
