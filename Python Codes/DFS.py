# DFS function (recursive)
def dfs(graph, vertex, visited):
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs(graph, neighbor, visited)

# Take user input for graph
graph = {}
n = int(input("Enter number of vertices: "))
for i in range(n):
    vertex = input(f"Enter vertex {i+1} name: ")
    neighbors = input(f"Enter neighbors of {vertex} separated by spaces: ").split()
    graph[vertex] = neighbors

# Take starting node from user
start_node = input("Enter starting vertex for DFS: ")

# Run DFS
print("DFS Traversal:", end=" ")
dfs(graph, start_node, set())
print()
