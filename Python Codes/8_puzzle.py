from collections import deque

# Function to display puzzle in a readable form
def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Function to get possible moves
def get_neighbors(state):
    neighbors = []
    idx = state.index('0')  # '0' represents the empty tile
    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }
    for move in moves[idx]:
        new_state = list(state)
        new_state[idx], new_state[move] = new_state[move], new_state[idx]
        neighbors.append(''.join(new_state))
    return neighbors

# BFS to solve the puzzle
def bfs(start, goal):
    visited = set()
    queue = deque([(start, [])])
    
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        
        if state not in visited:
            visited.add(state)
            for neighbor in get_neighbors(state):
                queue.append((neighbor, path + [state]))
    return None

# Take input from user
print("Enter initial state of 8-puzzle (use 0 for empty space, enter row-wise):")
initial_state = ''.join(input().split())
print("Enter goal state of 8-puzzle (use 0 for empty space, enter row-wise):")
goal_state = ''.join(input().split())

# Solve the puzzle
solution = bfs(initial_state, goal_state)

# Display the solution
if solution:
    print("\nSolution steps:")
    for step in solution:
        display(step)
else:
    print("No solution found!")
