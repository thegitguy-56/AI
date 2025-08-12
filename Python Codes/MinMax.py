import copy

# Initialize the board
def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check for winner
def check_winner(board):
    lines = board + [list(col) for col in zip(*board)]  # Rows and columns
    lines.append([board[i][i] for i in range(3)])        # Diagonal
    lines.append([board[i][2-i] for i in range(3)])      # Anti-diagonal

    for line in lines:
        if line == ['X'] * 3:
            return 'X'
        if line == ['O'] * 3:
            return 'O'
    return None

# Check if game is over
def game_over(board):
    return check_winner(board) is not None or all(cell != ' ' for row in board for cell in row)

# Evaluation function
def evaluate(board):
    winner = check_winner(board)
    if winner == 'X':
        return +10
    elif winner == 'O':
        return -10
    else:
        return 0

# Get possible moves
def get_possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# Make a move
def make_move(board, move, player):
    new_board = copy.deepcopy(board)
    i, j = move
    new_board[i][j] = player
    return new_board

# Minimax algorithm
def minimax(board, depth, player):
    if game_over(board) or depth == 0:
        return evaluate(board)

    if player == 'X':
        best_score = float('-inf')
        for move in get_possible_moves(board):
            new_board = make_move(board, move, 'X')
            score = minimax(new_board, depth - 1, 'O')
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_possible_moves(board):
            new_board = make_move(board, move, 'O')
            score = minimax(new_board, depth - 1, 'X')
            best_score = min(best_score, score)
        return best_score

# Find best move for AI
def find_best_move(board):
    best_score = float('-inf')
    best_move = None
    for move in get_possible_moves(board):
        new_board = make_move(board, move, 'X')
        score = minimax(new_board, depth=3, player='O')
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game loop (AI vs Human)
def play_game():
    board = init_board()
    print("Tic Tac Toe - You are 'O', AI is 'X'")
    print_board(board)

    while not game_over(board):
        # Human move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'O'
        print_board(board)

        if game_over(board):
            break

        # AI move
        print("AI is thinking...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)

    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")

# Run the game
play_game()
