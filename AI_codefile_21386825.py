# Standalone Code

# Necessary import
import heapq

# State representation and initialization
initial_state = ('E', 'E', 'E', 'E')
goal_state = ('W', 'W', 'W', 'W')

# Safety check function
def is_safe(state):
    farmer, wolf, goat, cabbage = state
    # Check if the wolf and goat are alone together
    if farmer != wolf and wolf == goat:
        return False
    # Check if the goat and cabbage are alone together
    if farmer != goat and goat == cabbage:
        return False
    return True

# Updated Possible Moves Function
def updated_possible_moves(state):
    farmer, wolf, goat, cabbage = state
    moves = []
    # Moves when the farmer is on the East side
    if farmer == 'E':
        # Farmer takes Wolf to West
        if is_safe(('W', 'W', goat, cabbage)):
            moves.append(('FW', ('W', 'W', goat, cabbage)))
        # Farmer takes Goat to West
        if is_safe(('W', wolf, 'W', cabbage)):
            moves.append(('FG', ('W', wolf, 'W', cabbage)))
        # Farmer takes Cabbage to West
        if is_safe(('W', wolf, goat, 'W')):
            moves.append(('FC', ('W', wolf, goat, 'W')))
        # Farmer goes alone to West
        if is_safe(('W', wolf, goat, cabbage)):
            moves.append(('F', ('W', wolf, goat, cabbage)))
    # Moves when the farmer is on the West side
    else:
        # Farmer takes Wolf to East
        if is_safe(('E', 'E', goat, cabbage)):
            moves.append(('FW', ('E', 'E', goat, cabbage)))
        # Farmer takes Goat to East
        if is_safe(('E', wolf, 'E', cabbage)):
            moves.append(('FG', ('E', wolf, 'E', cabbage)))
        # Farmer takes Cabbage to East
        if is_safe(('E', wolf, goat, 'E')):
            moves.append(('FC', ('E', wolf, goat, 'E')))
        # Farmer goes alone to East
        if is_safe(('E', wolf, goat, cabbage)):
            moves.append(('F', ('E', wolf, goat, cabbage)))
    return moves

# Display State Space function
def display_state_space(state, depth=1, max_depth=3, visited=None):
    if visited is None:
        visited = set()
    # Base cases: if the state is visited or depth exceeds max_depth
    if state in visited or depth > max_depth:
        return
    visited.add(state)
    # Check if the current state is safe
    if not is_safe(state):
        print('  ' * depth + str(state) + " (Unsafe/Dead End)")
        return
    else:
        print('  ' * depth + str(state))
    for _, new_state in updated_possible_moves(state):
        display_state_space(new_state, depth + 1, max_depth, visited)

# Heuristic function
def heuristic(state, goal_state):
    # Calculate the number of items not in their goal position
    return sum([1 for i in range(len(state)) if state[i] != goal_state[i]])

# DFS Algorithm
def dfs(start_state, goal_state):
    stack = [(start_state, [])]
    explored = set()
    while stack:
        state, path = stack.pop()
        if state == goal_state:
            return path
        if state not in explored:
            explored.add(state)
            for move, new_state in updated_possible_moves(state):
                stack.append((new_state, path + [move]))
    return None

# A* Search algorithm
def astar(start_state, goal_state):
    queue = [(0, start_state, [])]
    explored = set()
    while queue:
        cost, state, path = heapq.heappop(queue)
        if state == goal_state:
            return path
        if state not in explored:
            explored.add(state)
            for move, new_state in updated_possible_moves(state):
                new_cost = cost + 1
                priority = new_cost + heuristic(new_state, goal_state)
                heapq.heappush(queue, (priority, new_state, path + [move]))
    return None

def main_updated(start_state, goal_state):
    print('Starting state:', start_state)
    print('Goal state:', goal_state)
    
    print('\nState Space (limited to 3 levels deep):')
    display_state_space(start_state, max_depth=3)
    
    print('\nRunning DFS...')
    dfs_path = dfs(start_state, goal_state)
    if dfs_path:
        print('DFS path:')
        for move in dfs_path:
            if move == 'FW':
                print("Farmer takes Wolf")
            elif move == 'FG':
                print("Farmer takes Goat")
            elif move == 'FC':
                print("Farmer takes Cabbage")
            else:
                print("Farmer moves alone")
    else:
        print('No DFS path found')
        
    print('\nRunning A* search...')
    astar_path = astar(start_state, goal_state)
    if astar_path:
        print('A* search path:')
        for move in astar_path:
            if move == 'FW':
                print("Farmer takes Wolf")
            elif move == 'FG':
                print("Farmer takes Goat")
            elif move == 'FC':
                print("Farmer takes Cabbage")
            else:
                print("Farmer moves alone")
    else:
        print('No A* search path found')

# Running the completed main function
main_updated(initial_state, goal_state)