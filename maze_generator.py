import random

def generate_maze(x, y):
    # Initialize the maze with all walls (1s)
    maze = [[1] * (y + 2) for _ in range(x + 2)]

    # Set the starting position (1, 1) as an empty tile (0)
    maze[1][1] = 0

    # Set the ending position (y-1, x) as the exit (2)
    maze[y-1][x] = 2  # Set the ending position as the exit

    # Define the four possible directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Create a stack to keep track of the visited cells
    stack = [(1, 1)]

    while stack:
        # Get the current cell from the stack
        current_x, current_y = stack.pop()

        # Shuffle the directions randomly
        random.shuffle(directions)

        # Iterate over the shuffled directions
        for dx, dy in directions:
            # Calculate the new cell coordinates
            new_x, new_y = current_x + dx * 2, current_y + dy * 2

            # Check if the new cell is within the maze boundaries (including the border)
            if 1 <= new_x < x+1 and 1 <= new_y < y+1:
                # Check if the new cell is a wall (1)
                if maze[new_x][new_y] == 1:
                    # Make the new cell an empty tile (0)
                    maze[new_x][new_y] = 0

                    # Remove the wall between the current cell and the new cell
                    maze[current_x + dx][current_y + dy] = 0

                    # Add the new cell to the stack
                    stack.append((new_x, new_y))

    return maze
