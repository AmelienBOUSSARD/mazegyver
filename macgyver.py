import pygame
from pygame.locals import *

class Macgyver:
    """Class for create the character Macgyver"""

    def __init__(self, right, left, up, down, level):
                # Sprites du personnage
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        # Position du personnage en squares et en pixels
        self.square_x = 0
        self.square_y = 0
        self.x = 0
        self.y = 0
        # Direction par défaut
        self.axe = self.right
        # Niveau dans lequel le personnage se trouve
        self.level = level


def move(self, axe):
    """"move the character"""
    if axe == 'right':
        if self.square_x < (nbr_sprite_square - 1):
            if self.level.setting[self.square_y][self.square_x + 1] != '#':
                self.square_x += 1
                self.x = self.square_x * sprite_size
            self.axe = self.right

    if axe == 'left':
        if self.square_x < (nbr_sprite_square - 1):
            if self.level.setting[self.square_y][self.square_x + 1] != '#':
                self.square_x += 1
                self.x = self.square_x * sprite_size
            self.axe = self.left

    if axe == 'up':
        if self.square_x < (nbr_sprite_square - 1):
            if self.level.setting[self.square_y][self.square_x + 1] != '#':
                self.square_x += 1
                self.x = self.square_x * sprite_size
            self.axe = self.up

    if axe == 'down':
        if self.square_x < (nbr_sprite_square - 1):
            if self.level.setting[self.square_y][self.square_x + 1] != '#':
                self.square_x += 1
                self.x = self.square_x * sprite_size
            self.axe = self.down
