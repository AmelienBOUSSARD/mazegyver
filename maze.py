from constant import *
from macgyver import *


class Maze:
    """Class for create the Maze"""

    def __init__(self, file):
        self.file = file
        self.setting = 0

    # Generate the maze
    def generate(self):
        with open(self.file, "r") as file:
            level_setting = []
            for line in file:
                line_maze = []
                for sprite in line:
                    if sprite != '\n':
                        line_maze.append(sprite)

                level_setting.append(line_maze)

            self.setting = level_setting

    # Function for display the game
    def display(self, window):
        wall = pygame.image.load(img_wall).convert_alpha()
        guardian = pygame.image.load(img_guardian).convert_alpha()

        nbr_line = 0
        for line in self.setting:
            nbr_square = 0
            for sprite in line:
                x = nbr_square * sprite_size
                y = nbr_line * sprite_size
                if sprite == '#':
                    window.blit(wall, (x, y))
                elif sprite == 'G':
                    window.blit(guardian, (x, y))
                nbr_square += 1
            nbr_line += 1
