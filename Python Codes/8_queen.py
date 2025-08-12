# Program to solve the 8-Queen problem using Backtracking

# Function to print the chessboard
def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

# Check if placing a queen is safe
def is_safe(board, row, col):
    # Check this column in previous rows
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    
    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j]:
            return False
        i -= 1
        j += 1
    
    return True

# Solve function using backtracking
def solve_queens(board, row):
    if row == len(board):
        print_board(board)
        return True  # Found one solution, continue searching if needed
    
    res = False
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True
            res = solve_queens(board, row + 1) or res
            board[row][col] = False
    return res

# Take input from user for board size
n = int(input("Enter the number of queens (e.g., 8 for 8-Queens): "))

# Initialize board
board = [[False for _ in range(n)] for _ in range(n)]

# Solve the problem
if not solve_queens(board, 0):
    print("No solution exists!")
