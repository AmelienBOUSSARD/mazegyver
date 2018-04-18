import pygame
from pygame.locals import *
from constant import NBR_SPRITE_SQUARE, SPRITE_SIZE


class Macgyver:
    """Class for create the character Macgyver"""

    def __init__(self, right, left, up, down, LEVEL):
        """Constructor of the class"""
        # Sprites of character according to its axis
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        # Position of the character in squares and pixels
        self.square_x = 0
        self.square_y = 0
        self.var_x = 0
        self.var_y = 0
        # Axe by default
        self.axe = self.down
        # LEVEL in which the character is located
        self.level = LEVEL

    def move(self, axe):
        """"move the character"""
        if axe == 'right':
            if self.square_x < (NBR_SPRITE_SQUARE - 1):
                if not self.level.is_wall(self.square_y, self.square_x + 1):
                    self.square_x += 1
                    self.var_x = self.square_x * SPRITE_SIZE
            # axe of macgyver
            self.axe = self.right

        if axe == 'left':
            if self.square_x > 0:
                if not self.level.is_wall(self.square_y, self.square_x - 1):
                    self.square_x -= 1
                    self.var_x = self.square_x * SPRITE_SIZE
            # axe of macgyver
            self.axe = self.left

        if axe == 'up':
            if self.square_y > 0:
                if not self.level.is_wall(self.square_y - 1, self.square_x):
                    self.square_y -= 1
                    self.var_y = self.square_y * SPRITE_SIZE
            # axe of macgyver
            self.axe = self.up

        if axe == 'down':
            if self.square_y < (NBR_SPRITE_SQUARE - 1):
                if not self.level.is_wall(self.square_y + 1, self.square_x):
                    self.square_y += 1
                    self.var_y = self.square_y * SPRITE_SIZE
            # axe of macgyver
            self.axe = self.down
