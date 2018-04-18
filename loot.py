import random
from pygame.locals import *
from constant import SPRITE_SIZE


class Loot:
    """Class for create the loot"""

    def __init__(self, loot_img, LEVEL):
        """Constructor of the class"""
        self.square_y = 0
        self.square_x = 0
        self.level = LEVEL
        self.loaded = True
        self.loot_img = loot_img
        while self.loaded:
            # for random position use randint
            self.square_x = random.randint(1, 13)
            self.square_y = random.randint(1, 13)
            # verifying if passing so if 0
            if self.level.is_path(self.square_y, self.square_x):
                # location of the loot
                self.var_x = self.square_x * SPRITE_SIZE
                self.var_y = self.square_y * SPRITE_SIZE
                self.loaded = False
        # replace the 0 by a 1 where will be placed loot to avoid another loot this puts on
        self.level.set_loot(self.square_y, self.square_x)

    def display(self, loot_img, WINDOW):
        # location of the sprite of the loot image
        if self.level.is_loot(self.square_y, self.square_x):
            WINDOW.blit(self.loot_img, (self.var_x, self.var_y))
