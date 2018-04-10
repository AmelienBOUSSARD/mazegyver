import pygame
from pygame.locals import *
from constant import NBR_SPRITE_SQUARE, SPRITE_SIZE


class Macgyver:
    """Class for create the character Macgyver"""

    def __init__(self, right, left, up, down, LEVEL):
        """Constructor of the class"""
        # Sprites of character
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        # Position of the character in squares and pixels
        # -tc- Pas nécessaire de définir self.var_x et self.var_y.
        self.square_x = 0
        self.square_y = 0
        self.var_x = 0
        self.var_y = 0
        # Axe by default
        self.axe = self.down
        # LEVEL in which the character is located
        self.level = LEVEL

    # -tc- beaucoup de code répétitif dans cette méthode. Il y a certainement
    # -tc- moyen de factoriser
    def move(self, axe):
        """"move the character"""
        if axe == 'right':
            if self.square_x < (NBR_SPRITE_SQUARE - 1):
                # -tc- éviter d'accéder à self.level.setting directement
                if self.level.setting[self.square_y][self.square_x + 1] != '#':
                    self.square_x += 1
                    # -tc- par vraiment nécessaire
                    self.var_x = self.square_x * SPRITE_SIZE
            self.axe = self.right

        if axe == 'left':
            if self.square_x > 0:
                # -tc- éviter d'accéder à self.level.setting directement
                if self.level.setting[self.square_y][self.square_x - 1] != '#':
                    self.square_x -= 1
                    # -tc- par vraiment nécessaire
                    self.var_x = self.square_x * SPRITE_SIZE
            self.axe = self.left

        if axe == 'up':
            if self.square_y > 0:
                # -tc- éviter d'accéder à self.level.setting directement
                if self.level.setting[self.square_y - 1][self.square_x] != '#':
                    self.square_y -= 1
                    # -tc- par vraiment nécessaire
                    self.var_y = self.square_y * SPRITE_SIZE
            self.axe = self.up

        if axe == 'down':
            if self.square_y < (NBR_SPRITE_SQUARE - 1):
                # -tc- éviter d'accéder à self.level.setting directement
                if self.level.setting[self.square_y + 1][self.square_x] != '#':
                    self.square_y += 1
                    # -tc- par vraiment nécessaire
                    self.var_y = self.square_y * SPRITE_SIZE
            self.axe = self.down
