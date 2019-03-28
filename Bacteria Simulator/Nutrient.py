import random
from Config import Config
from Ocean import Ocean
from WorldObject import WorldObject


class Nutrient(WorldObject):

    radius = 2
    color = 0, 0, 0

    def __init__(self):

        super().__init__()

        self.x = random.randrange(Config.world_size[0])
        self.y = random.randrange(Config.world_size[1])
        self.size = Nutrient.radius

        self.isAlive = True

    def update(self):

        if self.isAlive:
            self.x, self.y = Ocean.drift(self)
            super().render(0)

    def die(self):

        self.x, self.y = -100, -100
        self.isAlive = False
