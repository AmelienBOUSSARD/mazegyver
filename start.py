#!/usr/bin/python3
# -*- coding: Utf-8 -*

# -tc- éviter d'importer de cette manière. La meilleure manière est
# -tc- de faire que Game soit une classe.
from game import *

# -tc- Problème: game est initialisé dans ton fichier de constantes. pas très 
# -tc- naturel, car ce n'est pas une constante.
while game:

    pygame.time.Clock().tick(30)
    pygame.display.set_icon(ICO)
    pygame.display.set_caption(TITLE_WINDOW)

    # For leave the program

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                MG.move('right')
            elif event.key == K_LEFT:
                MG.move('left')
            elif event.key == K_UP:
                MG.move('up')
            elif event.key == K_DOWN:
                MG.move('down')
    
    # -tc- tu relis ton fichier maze.txt et regénère ton labyrinthe à chaque tour
    # -tc- de boucle? Pas très efficace. En principe, tu n'as pas besoin de 
    # -tc- lire ton fichier plus d'une fois.
    LEVEL.generate()
    WINDOW.blit(BACKGROUND, (0, 0))
    LEVEL.display(WINDOW)
    WINDOW.blit(MG.axe, (MG.var_x, MG.var_y))
    # Refresh the display
    pygame.display.flip()

    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
        game = False
    # -tc- La fin du jeu n'est pas sur le gardien, mais devant le gardien
    if LEVEL.setting[MG.square_y][MG.square_x] == 'G':
        print("You WIN!!!")
        game = False
