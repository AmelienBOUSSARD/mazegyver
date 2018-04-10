from constant import IMG_WALL, IMG_GUARDIAN
# -tc- éviter les from module import *
from macgyver import *


# -tc- Pourquoi un underscore devant Maze?
class _Maze:
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

    def display(self, window):
        """Function for display the game"""
        wall = pygame.image.load(IMG_WALL).convert_alpha()
        guardian = pygame.image.load(IMG_GUARDIAN).convert_alpha()

        # utiliser la fonction enumerate() pour gérer nbr_line et nbr_square
        nbr_line = 0
        for line in self.setting:
            nbr_square = 0
            for sprite in line:
                var_x = nbr_square * SPRITE_SIZE
                var_y = nbr_line * SPRITE_SIZE
                if sprite == '#':
                    window.blit(wall, (var_x, var_y))
                elif sprite == 'G':
                    window.blit(guardian, (var_x, var_y))
                nbr_square += 1
            nbr_line += 1
