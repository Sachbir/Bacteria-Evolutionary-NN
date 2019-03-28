from Config import Config


class Ocean:

    @staticmethod
    def drift(obj):

        x = obj.x + 0.2 / obj.size * Config.drift_multiplier
        y = obj.y + 0.06 / obj.size * Config.drift_multiplier

        x %= Config.world_size[0]
        y %= Config.world_size[1]

        return x, y
