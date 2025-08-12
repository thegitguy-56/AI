from itertools import permutations

# Function to calculate the total distance of a given path
def calculate_distance(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    distance += graph[path[-1]][path[0]]  # Return to starting point
    return distance

# Take input from user
n = int(input("Enter number of cities: "))
cities = [str(i) for i in range(n)]
graph = {}

print("\nEnter the distance matrix (space-separated, row-wise):")
for i in range(n):
    row = list(map(int, input().split()))
    graph[str(i)] = {str(j): row[j] for j in range(n)}

# Solve TSP using brute force (permutations)
min_path = None
min_distance = float('inf')

for perm in permutations(cities[1:]):  # Fix the first city to avoid duplicates
    path = ['0'] + list(perm)
    dist = calculate_distance(graph, path)
    if dist < min_distance:
        min_distance = dist
        min_path = path

# Display result
print("\nMinimum cost path:", " -> ".join(min_path), "-> 0")
print("Minimum distance:", min_distance)
