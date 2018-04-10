import random
import pygame
from pygame.locals import *
from constant import IMG_ICO, TITLE_WINDOW, IMG_BACKGROUND, C_TUBE, C_NEEDLE, C_ETHER, MAZE, game
from maze import Maze
from loot import Loot
from macgyver import Macgyver


pygame.init()

# VAR
WINDOW = pygame.display.set_mode((450, 450))
ICO = pygame.image.load(IMG_ICO)
LEVEL = Maze(MAZE)
LEVEL.generate()
BACKGROUND = pygame.image.load(IMG_BACKGROUND).convert()
WINDOW.blit(BACKGROUND, (0, 0))
LEVEL.display(WINDOW)
MG = Macgyver("images/macgyver_right.png", "images/macgyver_left.png",
              "images/macgyver_up.png", "images/macgyver_down.png", LEVEL)
# Load loot
TUBE_IMG = pygame.image.load(C_TUBE).convert_alpha()
NEEDLE_IMG = pygame.image.load(C_NEEDLE).convert_alpha()
ETHER_IMG = pygame.image.load(C_ETHER).convert_alpha()

# Sprite of loot
TUBE = Loot(TUBE_IMG, LEVEL)
TUBE.display(TUBE_IMG, WINDOW)
NEEDLE = Loot(NEEDLE_IMG, LEVEL)
NEEDLE.display(NEEDLE_IMG, WINDOW)
ETHER = Loot(ETHER_IMG, LEVEL)
ETHER.display(ETHER_IMG, WINDOW)
