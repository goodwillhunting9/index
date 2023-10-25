import heapq

initial_state = ('E', 'E', 'E', 'E')
goal_state = ('W', 'W', 'W', 'W')

def is_safe(state):
    farmer, wolf, goat, cabbage = state
    if farmer != wolf and wolf == goat:
        return False
    if farmer != goat and goat == cabbage:
        return False
    return True

def possible_moves(state):
    farmer, wolf, goat, cabbage = state
    moves = []
    if farmer == wolf:
        moves.append(('FW', ('W' if farmer == 'E' else 'E', 'W' if wolf == 'E' else 'E', goat, cabbage)))
    if farmer == goat:
        moves.append(('FG', ('W' if farmer == 'E' else 'E', wolf, 'W' if goat == 'E' else 'E', cabbage)))
    if farmer == cabbage:
        moves.append(('FC', ('W' if farmer == 'E' else 'E', wolf, goat, 'W' if cabbage == 'E' else 'E')))
    moves.append(('F', ('W' if farmer == 'E' else 'E', wolf, goat, cabbage)))
    return moves

def dfs(start_state, goal_state):
    stack = [(start_state, [])]
    explored = set()
    while stack:
        state, path = stack.pop()
        if state == goal_state:
            return path + [state]
        if state not in explored:
            explored.add(state)
            for _, new_state in possible_moves(state):
                stack.append((new_state, path + [state]))
    return None

def heuristic(state, goal_state):
    return sum([1 for i in range(len(state)) if state[i] != goal_state[i]])

def astar(start_state, goal_state):
    queue = [(0, start_state, [])]
    explored = set()
    while queue:
        cost, state, path = heapq.heappop(queue)
        if state == goal_state:
            return path + [state]
        if state not in explored:
            explored.add(state)
            for move, new_state in possible_moves(state):
                new_cost = cost + 1
                priority = new_cost + heuristic(new_state, goal_state)
                heapq.heappush(queue, (priority, new_state, path + [state]))
    return None

def main():
    print('Starting state:', initial_state)
    print('Goal state:', goal_state)
    print('\nRunning DFS...')
    dfs_path = dfs(initial_state, goal_state)
    if dfs_path:
        print('DFS path:', dfs_path)
    else:
        print('No DFS path found')
    print('\nRunning A* search...')
    astar_path = astar(initial_state, goal_state)
    if astar_path:
        print('A* search path:', astar_path)
    else:
        print('No A* search path found')
