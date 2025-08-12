from collections import deque

# Function to check if a state is valid
def is_valid(state):
    m_left, c_left, m_right, c_right, _ = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

# Generate next possible states
def get_next_states(state):
    m_left, c_left, m_right, c_right, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # (M, C)
    next_states = []

    for m, c in moves:
        if boat == 'left':
            new_state = (m_left - m, c_left - c,
                         m_right + m, c_right + c, 'right')
        else:
            new_state = (m_left + m, c_left + c,
                         m_right - m, c_right - c, 'left')

        if is_valid(new_state):
            next_states.append(new_state)
    return next_states

# BFS to solve the problem
def missionaries_cannibals(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        if state not in visited:
            visited.add(state)
            for next_state in get_next_states(state):
                queue.append((next_state, path + [state]))
    return None

# Take input from user
m = int(input("Enter number of missionaries: "))
c = int(input("Enter number of cannibals: "))

# Initial and goal states
start_state = (m, c, 0, 0, 'left')  # (M_left, C_left, M_right, C_right, boat)
goal_state = (0, 0, m, c, 'right')

# Solve problem
solution = missionaries_cannibals(start_state, goal_state)

# Display solution
if solution:
    print("\nSteps to solve the problem:")
    for step in solution:
        print(step)
else:
    print("No solution found!")
