import sys

# Constants for player and opponent
PLAYER = 'X'
OPPONENT = 'O'

def print_board(board):
    # Function to print the Tic-Tac-Toe board
    for row in board:
        print(' | '.join(row))
        print('---------')

def evaluate(board):
    # Function to evaluate the current state of the board
    # and determine the winner or draw

    # Checking rows for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == PLAYER:
                return 1
            elif board[row][0] == OPPONENT:
                return -1

    # Checking columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == PLAYER:
                return 10
            elif board[0][col] == OPPONENT:
                return -10

    # Checking diagonals for a win
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == PLAYER:
            return 10
        elif board[0][0] == OPPONENT:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == PLAYER:
            return 10
        elif board[0][2] == OPPONENT:
            return -10

    # No winner, it's a draw
    return 0

def is_moves_left(board):
    # Function to check if there are any empty cells left on the board
    for row in board:
        for cell in row:
            if cell == ' ':
                return True
    return False

def minmax(board, depth, is_maximizer):
    # Minimax algorithm implementation

    # Evaluate the current state of the board
    score = evaluate(board)

    # If the maximizer or minimizer has won, return the score
    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth
    # If it's a draw, return 0
    elif not is_moves_left(board):
        return 0

    if is_maximizer:
        # Maximizing player's turn
        best_score = -sys.maxsize
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = PLAYER
                    best_score = max(best_score, minmax(board, depth + 1, not is_maximizer))
                    board[row][col] = ' '
        return best_score
    else:
        # Minimizing opponent's turn
        best_score = sys.maxsize
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = OPPONENT
                    best_score = min(best_score, minmax(board, depth + 1, not is_maximizer))
                    board[row][col] = ' '
        return best_score

def find_best_move(board):
    # Function to find the best move for the current player using the Minimax algorithm

    best_score = -sys.maxsize
    best_move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = PLAYER
                score = minmax(board, 0, False)
                board[row][col] = ' '

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

def play_game():
    # Function to start and play the Tic-Tac-Toe game

    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("Player: X, Opponent: O")
    print_board(board)

    while is_moves_left(board):
        # Player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = PLAYER
            print_board(board)
        else:
            print("Invalid move. Try again.")
            continue

        # Check if the player has won
        if evaluate(board) == 10:
            print("Congratulations! You win!")
            return

        if not is_moves_left(board):
            print("It's a draw!")
            return

        # Opponent's move
        print("Opponent is making a move...")
        move = find_best_move(board)
        board[move[0]][move[1]] = OPPONENT
        print_board(board)

        # Check if the opponent has won
        if evaluate(board) == -10:
            print("You lose!")
            return

    print("It's a draw!")

# Start the game
play_game()
