import pygame
import sys
from config import MAZE_WIDTH, MAZE_HEIGHT, CELL_SIZE

WHITE = (255, 255, 255)  # Empty cell
BLACK = (0, 0, 0)        # Wall
BLUE = (45, 208, 255)    # Path
RED = (255, 0, 0)        # Current position

CELL_SIZE = 10

def init_screen(width=MAZE_WIDTH, height=MAZE_HEIGHT):
    pygame.init()
    return pygame.display.set_mode((width * CELL_SIZE, height * CELL_SIZE))

def get_cell_color(cell_value):
    """Returns the color corresponding to the cell value."""
    colors = {0: WHITE, 1: BLACK, 2: WHITE, 3: BLUE, 4: RED}
    return colors[cell_value]

def draw_maze(maze, screen):
    """Draws the maze on the screen."""
    for y, row in enumerate(maze):
        for x, cell_value in enumerate(row):
            cell_color = get_cell_color(cell_value)
            pygame.draw.rect(screen, cell_color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

def keep_screen_open():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
