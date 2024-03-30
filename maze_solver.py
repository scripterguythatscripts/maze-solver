from collections import deque
import heapq
from maze_visualizer import draw_maze
from config import MAZE_WIDTH, MAZE_HEIGHT, TICK_SPEED

def heuristic(a, b):
    """Calculates the Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def remove_current_positions(maze, screen):
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 4:
                maze[y][x] = 3
    draw_maze(maze, screen)

def breadth_first_search(maze, start_pos, screen, clock):
    """Solves the maze using a breadth-first search algorithm."""
    current_positions = deque([start_pos])
    found_exit = False

    while current_positions and not found_exit:
        x, y = current_positions.popleft()

        maze[y][x] = 3  # Mark the current cell as part of the path

        # Check all adjacent cells
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy

            # Check if we've reached the exit
            if maze[new_y][new_x] == 2:
                maze[new_y][new_x] = 3
                found_exit = True
                break

            # Check if the cell is within bounds and is either empty or the exit
            if 0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT:
                if maze[new_y][new_x] in (0, 2):  # Empty or exit
                    current_positions.append((new_x, new_y))
                    maze[new_y][new_x] = 4  # Mark as a temporary part of the path

        draw_maze(maze, screen)
        clock.tick(TICK_SPEED)  # Adjust the tick rate


    # Remove temporary red markers
    remove_current_positions(maze, screen)

    return found_exit

def a_star_search(maze, start, goal, screen, clock):
    """Solves the maze using the A* search algorithm."""
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    found_exit = False

    while frontier and not found_exit:
        current = heapq.heappop(frontier)[1]

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_cell = (current[0] + dx, current[1] + dy)
            if 0 <= next_cell[0] < MAZE_WIDTH + 1 and 0 <= next_cell[1] < MAZE_HEIGHT + 1:
                if maze[next_cell[1]][next_cell[0]] in (0, 2):  # Check if the cell is walkable or the exit
                    if maze[next_cell[1]][next_cell[0]] == 2:  # Check if the cell is the exit
                        found_exit = True
                        came_from[next_cell] = current
                        break

                    new_cost = cost_so_far[current] + 1
                    if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                        cost_so_far[next_cell] = new_cost
                        priority = new_cost + heuristic(goal, next_cell)
                        heapq.heappush(frontier, (priority, next_cell))
                        came_from[next_cell] = current
                        # Mark the cell as visited
                        maze[next_cell[1]][next_cell[0]] = 4

        # Draw the current cell as the current position
        maze[current[1]][current[0]] = 3
        draw_maze(maze, screen)
        clock.tick(TICK_SPEED)

    if found_exit:
        # Mark the goal cell as part of the path
        maze[goal[1]][goal[0]] = 3
        print("Done!")

    remove_current_positions(maze, screen)

    return found_exit

def solve_maze(maze, start_pos, algorithm, screen, clock):
    """Solves the maze using the specified algorithm."""
    if algorithm == "a_star_search":
        exit_pos = (MAZE_WIDTH, MAZE_HEIGHT-1)
        return a_star_search(maze, start_pos, exit_pos, screen, clock)
    elif algorithm == "breadth_first_search":
        return breadth_first_search(maze, start_pos, screen, clock)
    else:
        raise ValueError("Unknown algorithm")