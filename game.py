import random

# -tc séparer les imports de la bibliothèque standard des autres
import pygame
from pygame.locals import *

# -tc séparer ses propres imports des bibliothèques tièrces
from constant import IMG_ICO, TITLE_WINDOW, IMG_BACKGROUND, C_TUBE, C_NEEDLE, C_ETHER, MAZE, game
# -tc- pourquoi un underscore devant Maze?
from maze import _Maze
from loot import Loot
from macgyver import Macgyver

# -tc- utiliser une classe pour représenter l'application
pygame.init()

# VAR
WINDOW = pygame.display.set_mode((450, 450))
ICO = pygame.image.load(IMG_ICO)
LEVEL = _Maze(MAZE)
BACKGROUND = pygame.image.load(IMG_BACKGROUND).convert()
MG = Macgyver("images/macgyver_right.png", "images/macgyver_left.png",
              "images/macgyver_up.png", "images/macgyver_down.png", LEVEL)
# Load loot
TUBE_IMG = pygame.image.load(C_TUBE).convert_alpha()
NEEDLE_IMG = pygame.image.load(C_NEEDLE).convert_alpha()
ETHER_IMG = pygame.image.load(C_ETHER).convert_alpha()

# -tc- ne pas utiliser des majuscules pour représenter des variables!
# Sprite of loot
TUBE = Loot(TUBE_IMG, LEVEL)
TUBE.display(TUBE_IMG, WINDOW)
NEEDLE = Loot(NEEDLE_IMG, LEVEL)
NEEDLE.display(NEEDLE_IMG, WINDOW)
ETHER = Loot(ETHER_IMG, LEVEL)
ETHER.display(ETHER_IMG, WINDOW)

# -tc- ne pas avoir de code executable en dessus de la condition if __name__ == "__main__"
