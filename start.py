#!/usr/bin/python3
# -*- coding: Utf-8 -*
import random
import time

import pygame
from pygame.locals import *
from constant import IMG_ICO, TITLE_WINDOW, IMG_BAG, IMG_IN_BAG
from constant import IMG_BACKGROUND, C_TUBE, C_NEEDLE, C_ETHER, MAZE
from maze import Maze
from loot import Loot
from macgyver import Macgyver


class Start:
    """Class for create start"""

    def __init__(self):
        """Constructor of the class"""
        pygame.init()
        # inivible cursor
        pygame.mouse.set_cursor(
            (8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
        # set size of window
        WINDOW = pygame.display.set_mode((450, 450))
        # set icon of window
        ICO = pygame.image.load(IMG_ICO)
        # load the level
        LEVEL = Maze(MAZE)
        # generate the level
        LEVEL.generate()
        # load BACKGROUND
        BACKGROUND = pygame.image.load(IMG_BACKGROUND).convert()
        # load BAG and IN_BAG
        BAG = pygame.image.load(IMG_BAG).convert_alpha()
        IN_BAG = pygame.image.load(IMG_IN_BAG).convert_alpha()
        # display BACKGROUND
        WINDOW.blit(BACKGROUND, (0, 0))
        # display maze
        LEVEL.display(WINDOW)
        # display BAG and IN_BAG
        WINDOW.blit(BAG, (0, 418))
        WINDOW.blit(IN_BAG, (37, 418))
        # load MAZE_SONG
        MAZE_SONG = pygame.mixer.Sound("maze_song.ogg")
        # play song
        MAZE_SONG.play(loops=-1, maxtime=0, fade_ms=0)
        # load Macgyver sprites according to the axis
        MG = Macgyver(
            "images/macgyver_right.png",
            "images/macgyver_left.png",
            "images/macgyver_up.png",
            "images/macgyver_down.png",
            LEVEL)
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
        # Var
        game = True
        Tube_Picked = False
        Ether_Picked = False
        Needle_Picked = False
        YOU_WIN = False
        YOU_LOSE = False

        print("Incoming transmiton...")

        while game:

            pygame.time.Clock().tick(30)
            pygame.display.set_icon(ICO)
            pygame.display.set_caption(TITLE_WINDOW)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # display BACKGROUND
                    WINDOW.blit(BACKGROUND, (0, 0))
                    # display maze
                    LEVEL.display(WINDOW)
                    # display BAG and IN_BAG
                    WINDOW.blit(BAG, (0, 418))
                    WINDOW.blit(IN_BAG, (37, 418))
                    if Tube_Picked is False:
                        TUBE.display(TUBE_IMG, WINDOW)
                    if Tube_Picked is True:
                        WINDOW.blit(TUBE_IMG, (40, 418))
                    if Ether_Picked is False:
                        ETHER.display(ETHER_IMG, WINDOW)
                    if Ether_Picked is True:
                        WINDOW.blit(ETHER_IMG, (75, 418))
                    if Needle_Picked is False:
                        NEEDLE.display(NEEDLE_IMG, WINDOW)
                    if Needle_Picked is True:
                        WINDOW.blit(NEEDLE_IMG, (110, 418))
                    if event.key == K_RIGHT:
                        MG.move('right')
                    elif event.key == K_LEFT:
                        MG.move('left')
                    elif event.key == K_UP:
                        MG.move('up')
                    elif event.key == K_DOWN:
                        MG.move('down')
            # Display MacGyver
            WINDOW.blit(MG.axe, (MG.var_x, MG.var_y))
            # Refresh the display
            pygame.display.flip()
            # take the TUBE if Macgyver is on the TUBE
            if (MG.var_x, MG.var_y) == (TUBE.var_x, TUBE.var_y):
                Tube_Picked = True
            # take ETHER if Macgyver is on the ETHER
            if (MG.var_x, MG.var_y) == (ETHER.var_x, ETHER.var_y):
                Ether_Picked = True
            # take NEEDLE if Macgyver is on the NEEDLE
            if (MG.var_x, MG.var_y) == (NEEDLE.var_x, NEEDLE.var_y):
                Needle_Picked = True

            if (event.type == QUIT or event.type == KEYDOWN and
                    event.key == K_ESCAPE):
                game = False

            # EndGame Victory or lose
            # if macgyver arrives in front of the guard
            if LEVEL.setting[MG.square_y][MG.square_x] == 'S':
                # loot check
                if (Tube_Picked is True and Needle_Picked is True and
                        Ether_Picked is True):
                    YOU_WIN = True
                else:
                    YOU_LOSE = True

                if YOU_WIN is True:
                    # \033[1;33;40m is for color the shell but does not always work
                    print("\033[1;33;40m \n       ...............\n   ,,,,,.           .,,,,,\n   ,,  ,,    YOU    ,,  ,,\n    ,. ,,    WIN    ,, .,\n     ,, ,,   !!!   ,, ,,\n       ,,,,       ,,,,\n           ,,   ,,\n             ,,,\n              ,\n           ,,,,,,\n        ,,,,,,,,,,,,,")
                    print("  Thank's to play my game \nTHREE")
                    time.sleep(1)
                    print("TWO")
                    time.sleep(1)
                    print("ONE")
                    time.sleep(1)
                    print("End of transmission...")
                    game = False

                if YOU_LOSE is True:
                    # \033[1;30;47m is for color the shell but does not always work
                    print("\033[1;30;47m \n              @@@@@ @@@@@\n           @               @\n         @        YOU        @\n         @       DEAD        @\n          @                 @\n         @ @               @ @\n          @@ @@@@@   @@@@@ @@\n     @     @ @@@@     @@@@ @    @@\n    @  @   @      @ @          @  @\n   @      @@@@    @ @    @@@@      @\n        @@   @@@       @@@   @@\n            @@   @@@@@@  @@\n           @@@  @@@@@@@@ @@@\n     @ @@    @@         @@    @  @\n      @   @      @@@@@      @   @\n       @@                     @@ \n")
                    print("THREE")
                    time.sleep(1)
                    print("TWO")
                    time.sleep(1)
                    print("ONE")
                    time.sleep(1)
                    print("End of transmission...")
                    game = False


if __name__ == '__main__':
    Start()
