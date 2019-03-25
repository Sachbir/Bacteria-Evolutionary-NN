import pygame
import sys
from Bacteria import Bacteria
from Config import Config
from Nutrient import Nutrient


class World:

    # pygame.init()
    # screen = pygame.display.set_mode(Config.world_size)
    # clock = pygame.time.Clock()

    def __init__(self):

        print("\n---INITIALIZE---")

    def run(self):

        bacteria = [Bacteria()]
        nutrients = [Nutrient(),
                     Nutrient(),
                     Nutrient(),
                     Nutrient(),
                     Nutrient()]

        while True:
            self.process_events()

            World.screen.fill(Config.background_color)  # Off-white

            bacteria_that_reproduce = []

            for i in range(len(bacteria)):
                successful_reproduction = bacteria[i].update(nutrients)
                if successful_reproduction:
                    bacteria_that_reproduce.append(i)

            for i in range(len(bacteria_that_reproduce)):
                index_of_reproducer = bacteria_that_reproduce[i]
                del bacteria[index_of_reproducer]
            for i in range(len(bacteria_that_reproduce)):
                bacteria.append(Bacteria())
                bacteria.append(Bacteria())

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


# world = World()
# world.run()


profit = 6.7                   # millions
rate_of_return = 15*60                  # seconds
cost_of_upgrade = 1.5        # millions

ROI = cost_of_upgrade / (profit / rate_of_return)
minutes_to_ROI = ROI / 60

print("\nIt takes " + str(minutes_to_ROI) + " minutes to get your money back")
