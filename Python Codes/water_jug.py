from collections import deque

# Function to check if we have reached the goal
def is_goal(state, target):
    return target in state

# Function to get next possible states
def get_next_states(state, capacities):
    a, b = state
    max_a, max_b = capacities
    states = []

    # Fill jug A
    states.append((max_a, b))
    # Fill jug B
    states.append((a, max_b))
    # Empty jug A
    states.append((0, b))
    # Empty jug B
    states.append((a, 0))
    # Pour A -> B
    pour = min(a, max_b - b)
    states.append((a - pour, b + pour))
    # Pour B -> A
    pour = min(b, max_a - a)
    states.append((a + pour, b - pour))

    return states

# BFS to solve water jug problem
def water_jug_solver(capacities, target):
    start = (0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if is_goal(state, target):
            return path + [state]

        if state not in visited:
            visited.add(state)
            for next_state in get_next_states(state, capacities):
                queue.append((next_state, path + [state]))
    return None

# Take user input
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount of water: "))

# Solve problem
solution = water_jug_solver((jug1, jug2), target)

# Display solution
if solution:
    print("\nSteps to reach target:")
    for step in solution:
        print(step)
else:
    print("No solution possible!")
