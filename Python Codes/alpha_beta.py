# Alpha-Beta Pruning Algorithm Implementation

def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, maxDepth):
    if depth == maxDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float("-inf")
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Beta cut-off
        return best
    else:
        best = float("inf")
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha cut-off
        return best

# Take user input for leaf values
values = list(map(int, input("Enter leaf node values separated by spaces: ").split()))
maxDepth = 0
nodes = len(values)

# Calculate maxDepth based on leaf count (binary tree)
while (2 ** maxDepth) < nodes:
    maxDepth += 1

# Run Alpha-Beta Pruning
result = alpha_beta(0, 0, True, values, float("-inf"), float("inf"), maxDepth)
print("\nThe optimal value is:", result)
