#!/usr/bin/python3
# -*- coding: Utf-8 -*

from game import *

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
