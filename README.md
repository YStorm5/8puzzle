# 8puzzle Solver

This is a Python function for solving the 8-puzzle game using the Breadth-First Search (BFS) algorithm.

## Usage

To use this solver, you can call the `bfs` function, which takes two parameters in the form of tuples:
1. The current state of the puzzle.
2. The goal state of the puzzle that you want to solve.

Here's an example of how to use the `bfs` function:

```python

# Define the initial and goal states as tuples
initial_state = (0,7,1,3,8,5,6,4,2)
goal_state = (1,2,3,4,5,6,7,8,0)

# Call the bfs function to solve the puzzle
bfs(initial_state, goal_state)

