import pygame
from pygame.locals import *
from constant import *
from maze import *
from macgyver import *


pygame.init()

# VAR
window = pygame.display.set_mode((450, 450))
ico = pygame.image.load(img_ico)
level = Maze(maze)
background = pygame.image.load(img_background).convert()
img = Macgyver("images/macgyver_right.png", "images/macgyver_left.png",
               "images/macgyver_up.png", "images/macgyver_down.png", level)

while game:
    pygame.time.Clock().tick(30)
    pygame.display.set_icon(ico)
    pygame.display.set_caption(title_window)
    level.generate()
    window.blit(background, (0, 0))
    level.display(window)
    # Refresh the display
    pygame.display.flip()

    # For leave the program
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            game = False
