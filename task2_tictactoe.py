import math

board = [" "] * 9

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(b):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in wins:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] != " ":
            return b[combo[0]]
    return None

def is_full(b):
    return " " not in b

def minimax(b, is_ai_turn):
    winner = check_winner(b)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_full(b):
        return 0

    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "O" if is_ai_turn else "X"
            scores.append(minimax(b, not is_ai_turn))
            b[i] = " "

    return max(scores) if is_ai_turn else min(scores)

def ai_move():
    best_score = -math.inf
    best_spot = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_spot = i
    board[best_spot] = "O"

def player_move():
    while True:
        try:
            choice = int(input("Enter position (1-9): ")) - 1
            if 0 <= choice <= 8 and board[choice] == " ":
                board[choice] = "X"
                break
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

print("Tic-Tac-Toe | You = X  |  AI = O")
print("Positions:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

while True:
    print_board()
    player_move()

    if check_winner(board) == "X":
        print_board()
        print("You win!")
        break
    if is_full(board):
        print_board()
        print("It's a draw!")
        break

    ai_move()

    if check_winner(board) == "O":
        print_board()
        print("AI wins!")
        break
    if is_full(board):
        print_board()
        print("It's a draw!")
        break