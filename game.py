import pygame
import random
from pygame.locals import *
from constant import *
from maze import _Maze
from macgyver import *


pygame.init()

# VAR
window = pygame.display.set_mode((450, 450))
ico = pygame.image.load(img_ico)
level = _Maze(maze)
background = pygame.image.load(img_background).convert()
mg = Macgyver("images/macgyver_right.png", "images/macgyver_left.png",
              "images/macgyver_up.png", "images/macgyver_down.png", level)

# if __name__ == "__main__":
# instance start et game
# call start for start the game


# tant que
