#!/usr/bin/python3
# -*- coding: Utf-8 -*

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
mg = Macgyver("images/macgyver_right.png", "images/macgyver_left.png",
              "images/macgyver_up.png", "images/macgyver_down.png", level)

while game:

    pygame.time.Clock().tick(30)
    pygame.display.set_icon(ico)
    pygame.display.set_caption(title_window)

    # For leave the program

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                mg.move('right')
            elif event.key == K_LEFT:
                mg.move('left')
            elif event.key == K_UP:
                mg.move('up')
            elif event.key == K_DOWN:
                mg.move('down')

    level.generate()
    window.blit(background, (0, 0))
    level.display(window)
    window.blit(mg.axe, (mg.x, mg.y))
    # Refresh the display
    pygame.display.flip()

    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
        game = False
    if level.setting[mg.square_y][mg.square_x] == 'G':
        print("You WIN!!!")
        game = False
