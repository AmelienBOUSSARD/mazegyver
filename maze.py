import pygame
from pygame.locals import *
from constant import *


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
        start = pygame.image.load(img_start).convert_alpha()
        guardian = pygame.image.load(img_guardian).convert_alpha()

        nbr_line = 0
        for line in self.setting:
            nbr_square = 0
            for sprite in line:
                x = nbr_square * sprite_size
                y = nbr_line * sprite_size
                if sprite == '#':
                    window.blit(wall, (x, y))
                elif sprite == 'M':
                    window.blit(start, (x, y))
                elif sprite == 'G':
                    window.blit(guardian, (x, y))
                nbr_square += 1
            nbr_line += 1


class Macgyver:
    """Class for create the character Macgyver"""

    def __init__(self, right, left, up, down, level):
                # Sprites du personnage
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        # Position du personnage en squares et en pixels
        self.square_x = 0
        self.square_y = 0
        self.x = 0
        self.y = 0
        # Direction par défaut
        self.axe = self.right
        # Niveau dans lequel le personnage se trouve
        self.level = level


def move(self, axe):
    """"move the character"""
    if axe == 'right':
        if self.square_x < (nbr_sprite_square - 1):
            if self.level.setting[self.square_y][self.square_x + 1] != '#':
                self.square_x += 1
                self.x = self.square_x * sprite_size
            self.axe = self.right

    if axe == 'left':
        if self.square_x < (nbr_sprite_square - 1):
            if self.level.setting[self.square_y][self.square_x + 1] != '#':
                self.square_x += 1
                self.x = self.square_x * sprite_size
            self.axe = self.left

    if axe == 'up':
        if self.square_x < (nbr_sprite_square - 1):
            if self.level.setting[self.square_y][self.square_x + 1] != '#':
                self.square_x += 1
                self.x = self.square_x * sprite_size
            self.axe = self.up

    if axe == 'down':
        if self.square_x < (nbr_sprite_square - 1):
            if self.level.setting[self.square_y][self.square_x + 1] != '#':
                self.square_x += 1
                self.x = self.square_x * sprite_size
            self.axe = self.down


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
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
            elif event.key == K_RIGHT:
                dk.deplacer('right')
            elif event.key == K_LEFT:
                dk.deplacer('left')
            elif event.key == K_UP:
                dk.deplacer('up')
            elif event.key == K_DOWN:
                dk.deplacer('down')
