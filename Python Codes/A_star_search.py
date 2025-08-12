from queue import PriorityQueue

# A* Search Algorithm
def a_star(graph, heuristic, start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    g_cost = {start: 0}
    came_from = {start: None}

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1], g_cost[goal]

        for neighbor, cost in graph[current].items():
            tentative_g = g_cost[current] + cost
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                pq.put((f_cost, neighbor))
                came_from[neighbor] = current

    return None, float("inf")

# Take input from user
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} with cost (format: neighbor:cost ...): ").split()
    graph[node] = {}
    for pair in neighbors:
        neighbor, cost = pair.split(":")
        graph[node][neighbor] = int(cost)

heuristic = {}
print("\nEnter heuristic values for each node:")
for node in graph:
    heuristic[node] = int(input(f"Heuristic for {node}: "))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# Run A* Algorithm
path, cost = a_star(graph, heuristic, start, goal)

# Display result
if path:
    print("\nPath found:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found!")
