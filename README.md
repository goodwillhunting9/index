problem: The Farmer, Wolf, Goat, and Cabbage problem is a classic puzzle in which a farmer must transport a wolf, a goat, and a cabbage across a river using a boat. The farmer can only carry one item at a time and cannot leave the wolf alone with the goat or the goat alone with the cabbage. The goal is to find a sequence of moves that allows the farmer to transport all three items across the river without any of them being eaten.


"Step-by-step Breakdown:

1. Initialization
Import the necessary modules (like heapq for priority queue operations in the A* search).
Define the initial and goal states. Both states are represented as tuples indicating the positions ('E' for East or 'W' for West) of the Farmer, Wolf, Goat, and Cabbage.

2. Safety Check Function (is_safe)
This function determines whether a given state is safe.
It checks two main conditions:
a. If the wolf and goat are together without the farmer.
b. If the goat and cabbage are together without the farmer.

3. Possible Moves Function (updated_possible_moves)
This function generates all possible moves from a given state considering safety constraints.
It determines moves based on the farmer's position (whether on the East or West side).
For each possible move, it checks if the resulting state is safe using the is_safe function.
Display State Space Function (display_state_space)
This function is designed to display the state space up to a certain depth.
It recursively explores each possible move, up to a given depth, and prints out the state.

4. Depth-First Search (DFS) Algorithm (dfs)
This function uses a stack to explore possible states.
It continues exploring until it finds the goal state or exhausts all possibilities.

5. A Search Algorithm (astar)*
This function uses a priority queue to explore states based on a cost function.
The cost function includes the cost to reach the current state and a heuristic estimating the cost to reach the goal state.
The heuristic used is a simple count of items not in their goal positions.
Like the DFS, it continues exploring until it finds the goal state or exhausts all possibilities.

6. Main Function (main_updated)
This function initializes the problem, displays the state space, and then runs both the DFS and A* search algorithms.
For each algorithm, it prints out the resulting path or indicates that no solution was found.
"
