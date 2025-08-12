# Map Coloring Problem using Constraint Satisfaction (Backtracking)

# Function to check if color assignment is valid
def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function
def backtrack(graph, colors, assignment):
    if len(assignment) == len(graph):
        return assignment

    unassigned = [node for node in graph if node not in assignment][0]

    for color in colors:
        if is_safe(unassigned, color, assignment, graph):
            assignment[unassigned] = color
            result = backtrack(graph, colors, assignment)
            if result:
                return result
            assignment.pop(unassigned)
    return None

# Take user input
graph = {}
n = int(input("Enter number of regions (nodes): "))
for i in range(n):
    region = input(f"Enter region {i+1} name: ")
    neighbors = input(f"Enter neighbors of {region} separated by spaces: ").split()
    graph[region] = neighbors

colors = input("\nEnter available colors separated by spaces: ").split()

# Solve CSP
solution = backtrack(graph, colors, {})

# Display result
if solution:
    print("\nColor Assignment:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No valid coloring found!")
