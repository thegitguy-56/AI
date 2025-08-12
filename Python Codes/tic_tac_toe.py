# Tic Tac Toe Game in Python

# Function to display the board
def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a win
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check for a draw
def is_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn.")

        # Take input from user
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_draw(board):
                display_board(board)
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move! Try again.")

# Run the game
tic_tac_toe()
