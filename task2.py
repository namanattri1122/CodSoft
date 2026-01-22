# Tic-Tac-Toe with Unbeatable AI
# Human = X, AI = O

board = [" " for _ in range(9)]

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def board_full():
    return " " not in board

def minimax(is_ai_turn):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if board_full():
        return 0

    if is_ai_turn:
        best_score = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                if score < best_score:
                    best_score = score
        return best_score

def ai_move():
    best_score = -100
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def human_move():
    while True:
        pos = int(input("Enter position (1-9): ")) - 1
        if 0 <= pos < 9 and board[pos] == " ":
            board[pos] = "X"
            break
        else:
            print("Invalid move. Try again.")

print("TIC TAC TOE")
print("You are X | AI is O")
show_board()

while True:
    human_move()
    show_board()

    if check_winner("X"):
        print("You win! (This should not happen 😄)")
        break
    if board_full():
        print("It's a draw!")
        break

    print("AI is thinking...")
    ai_move()
    show_board()

    if check_winner("O"):
        print("AI wins!")
        break
    if board_full():
        print("It's a draw!")
        break
