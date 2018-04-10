import random
import pygame
from pygame.locals import *
from constant import SPRITE_SIZE


class Loot:
    """Class for create the loot"""

    def __init__(self, loot_img, LEVEL):
        """Constructor of the class"""
        self.square_y = 0
        self.square_x = 0
        self.var_x = 0
        self.var_y = 0
        self.level = LEVEL
        self.loaded = True
        self.loot_img = loot_img
        while self.loaded:
            self.square_x = random.randint(0, 14)
            self.square_y = random.randint(0, 14)
            if self.level.setting[self.square_y][self.square_x] == '0':
                self.var_x = self.square_x * SPRITE_SIZE
                self.var_y = self.square_y * SPRITE_SIZE
                self.loaded = False
        self.level.setting[self.square_y][self.square_x] = '1'


    def display(self, loot_img, window):

        if self.level.setting[self.square_y][self.square_x] == '1':
            window.blit(self.loot_img, (self.var_x, self.var_y))
