
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")
        
def check_winner(board, player): # player can be "X" or "O"
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):
        return -10 + depth
    elif check_winner(board, "O"):
        return 10 - depth
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for move in available_moves(board):
            board[move[0]][move[1]] = "O"
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in available_moves(board):
            board[move[0]][move[1]] = "X"
            score = minimax(board, depth - 1, False)
            board[move[0]][move[1]] = " "
            best_score = min(score, best_score)
        return best_score

def computer_move(board):
    best_move = None
    best_score = float("-inf")
    for move in available_moves(board):
        board[move[0]][move[1]] = "O"
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = " "
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move[0]][best_move[1]] = "O"
    return board

def play_game():
    board = [[" " for row in range(3)] for col in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        board[1][1] = 0
        print_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break
        
        print("Computer's turn...")
        board = computer_move(board)
        print_board(board)
        
        if check_winner(board, "O"):
            print("Computer wins! You lose.")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

play_game()
