from constant import IMG_WALL, IMG_GUARDIAN, IMG_BAG
from macgyver import *


class Maze:
    """Class for create the Maze"""

    def __init__(self, file):
        self.file = file
        self.setting = 0

    def generate(self):
        """Generate the maze"""
        with open(self.file, "r") as file:
            level_setting = []
            for line in file:
                line_maze = []
                for sprite in line:
                    if sprite != '\n':
                        line_maze.append(sprite)

                level_setting.append(line_maze)

            self.setting = level_setting

    def display(self, WINDOW):
        """Function for display the game"""
        # load sprite of wall
        wall = pygame.image.load(IMG_WALL).convert_alpha()
        # load sprite of guardian
        guardian = pygame.image.load(IMG_GUARDIAN).convert_alpha()

        nbr_line = 0
        for line in self.setting:
            nbr_square = 0
            for sprite in line:
                var_x = nbr_square * SPRITE_SIZE
                var_y = nbr_line * SPRITE_SIZE
                if sprite == '#':
                    # display sprite of wall
                    WINDOW.blit(wall, (var_x, var_y))
                elif sprite == 'G':
                    # display sprite of guardian
                    WINDOW.blit(guardian, (var_x, var_y))
                nbr_square += 1
            nbr_line += 1
