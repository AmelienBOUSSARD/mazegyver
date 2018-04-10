#!/usr/bin/python3
# -*- coding: Utf-8 -*

from game import *

while game:

    pygame.time.Clock().tick(30)
    pygame.display.set_icon(ICO)
    pygame.display.set_caption(TITLE_WINDOW)

    # For leave the program

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            WINDOW.blit(BACKGROUND, (0, 0))
            LEVEL.display(WINDOW)
            TUBE.display(TUBE_IMG, WINDOW)
            NEEDLE.display(NEEDLE_IMG, WINDOW)
            ETHER.display(ETHER_IMG, WINDOW)
            if event.key == K_RIGHT:
                MG.move('right')
            elif event.key == K_LEFT:
                MG.move('left')
            elif event.key == K_UP:
                MG.move('up')
            elif event.key == K_DOWN:
                MG.move('down')

    WINDOW.blit(MG.axe, (MG.var_x, MG.var_y))

    # Refresh the display
    pygame.display.flip()

    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
        game = False
    if LEVEL.setting[MG.square_y][MG.square_x] == 'S':#if loot ramasser:
        print("You WIN!!!")
        game = False
