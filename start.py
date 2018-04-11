#!/usr/bin/python3
# -*- coding: Utf-8 -*

from game import *

# Var
game = True
nbr_loot = 0
Tube_Picked = False
Ether_Picked = False
Needle_Picked = False
pocket_loot = 0
font = pygame.font.Font(None, 30)
display_loot_nbr = font.render(
    str(int(nbr_loot)), True, pygame.Color('white'))
while game:

    pygame.time.Clock().tick(30)
    pygame.display.set_icon(ICO)
    pygame.display.set_caption(TITLE_WINDOW)

    # For leave the program

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            WINDOW.blit(BACKGROUND, (0, 0))
            LEVEL.display(WINDOW)
            if Tube_Picked == False:
                TUBE.display(TUBE_IMG, WINDOW)
            if Ether_Picked == False:
                ETHER.display(ETHER_IMG, WINDOW)
            if Needle_Picked == False:
                NEEDLE.display(NEEDLE_IMG, WINDOW)
            if event.key == K_RIGHT:
                MG.move('right')
            elif event.key == K_LEFT:
                MG.move('left')
            elif event.key == K_UP:
                MG.move('up')
            elif event.key == K_DOWN:
                MG.move('down')

    WINDOW.blit(MG.axe, (MG.var_x, MG.var_y))

    if (MG.var_x, MG.var_y) == (TUBE.var_x, TUBE.var_y):
        Tube_Picked = True

    if (MG.var_x, MG.var_y) == (ETHER.var_x, ETHER.var_y):
        Ether_Picked = True

    if (MG.var_x, MG.var_y) == (NEEDLE.var_x, NEEDLE.var_y):
        Needle_Picked = True

    # Refresh the display
    pygame.display.flip()

    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
        game = False

    # EndGame Victory or loose
    if LEVEL.setting[MG.square_y][MG.square_x] == 'S':
        if Tube_Picked is True and Needle_Picked is True and Ether_Picked is True:
            YOU_WIN = True
        else:
            YOU_LOOSE = True

        if YOU_WIN is True:
            print("You WIN !!! Thank's to play my game")
            game = False

        if YOU_LOOSE is True:
            print("You Loose !!!")
            game = False
