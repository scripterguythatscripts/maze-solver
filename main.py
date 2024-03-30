import pygame
from maze_generator import generate_maze
from maze_solver import solve_maze
from maze_visualizer import keep_screen_open, init_screen
from config import MAZE_WIDTH, MAZE_HEIGHT, CELL_SIZE

def main():
    maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
    start_pos = (0, 1)
    algorithm = "a_star_search"

    screen = init_screen(MAZE_WIDTH + 1, MAZE_HEIGHT + 1)
    clock = pygame.time.Clock()

    solved = solve_maze(maze, start_pos, algorithm, screen, clock)

    if solved:
        print("Maze solved!")
    else:
        print("No solution found.")

    keep_screen_open()

if __name__ == "__main__":
    main()