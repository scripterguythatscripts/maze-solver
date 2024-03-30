# Maze Solver Project

This project offers a Python framework for generating, solving, and visualizing mazes using various search algorithms. It's designed to be accessible for those with Python experience who are interested in exploring maze-solving techniques.

## Project Structure

The project is modularized into the following components:

- `maze_generator.py`:
  - Contains functions for generating mazes using algorithms like recursive backtracking.
  - Provides options to customize maze dimensions and complexity.

- `maze_solver.py`:
  - Houses implementations of search algorithms such as:
    - Breadth-First Search (BFS)
    - A* Search
  - Offers a common interface for integrating new algorithms.

- `maze_visualizer.py`:
  - Leverages the Pygame library to visualize mazes and solution paths.
  - Allows for interactive exploration and step-by-step visualization.

- `main.py`:
  - Serves as the entry point for the project.
  - Orchestrates maze generation, algorithm selection, and visualization.

- `config.py`:
   - Set parameters like width, height, cell size, and script execution speed here.
## Getting Started

Clone the repository:

```bash
git clone https://github.com/scripterguythatscripts/maze-solver.git
```

Install dependencies:

```bash
pip install pygame
```

Run the project:

```bash
python main.py
```

## Adding New Search Algorithms

The project is designed to facilitate the addition of custom search algorithms. Here's how:

1. Open the 'maze_solver.py' file.
2. Define a function for your algorithm, adhering to the following signature:

    ```python
    def your_algorithm(maze, start_pos, goal_pos, screen, clock):
        # Implement your algorithm logic here
        return solved  # Return whether or not the algorithm has found an exit
    ```

3. Integrate your algorithm into 'main.py' by calling it and passing the required parameters.
