from collections import deque

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    print("BFS Traversal:", end=" ")
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    print()

# Take user input for graph
graph = {}
n = int(input("Enter number of vertices: "))
for i in range(n):
    vertex = input(f"Enter vertex {i+1} name: ")
    neighbors = input(f"Enter neighbors of {vertex} separated by spaces: ").split()
    graph[vertex] = neighbors

# Take starting node from user
start_node = input("Enter starting vertex for BFS: ")

# Run BFS
bfs(graph, start_node)
