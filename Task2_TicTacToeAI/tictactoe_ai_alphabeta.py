# ----------------------------------------------------------
# CODSOFT - Task 2: Tic-Tac-Toe AI (with Alpha-Beta Pruning)
# Author: Sai Charan Koganti
# ----------------------------------------------------------

import math

# Initialize empty 3x3 board
board = [" " for _ in range(9)]

# ---------- Display the board ----------
def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# ---------- Utility functions ----------
def check_winner(player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw():
    return " " not in board

def available_moves():
    return [i for i, cell in enumerate(board) if cell == " "]

# ---------- Minimax with Alpha-Beta Pruning ----------
def minimax(is_maximizing, alpha, beta):
    if check_winner("O"):  # AI wins
        return 1
    elif check_winner("X"):  # Player wins
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves():
            board[move] = "O"
            eval = minimax(False, alpha, beta)
            board[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # 🧠 Prune unnecessary branches
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves():
            board[move] = "X"
            eval = minimax(True, alpha, beta)
            board[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # 🧠 Prune unnecessary branches
        return min_eval

# ---------- AI Move ----------
def ai_move():
    best_score = -math.inf
    best_move = None
    for move in available_moves():
        board[move] = "O"
        score = minimax(False, -math.inf, math.inf)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = "O"

# ---------- Main Game ----------
def play_game():
    print("🎮 Tic-Tac-Toe AI (with Alpha-Beta Pruning)")
    print("You are 'X' and AI is 'O'")
    print_board()

    while True:
        # Player move
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if board[pos] != " ":
                print("❌ Spot already taken, choose another.")
                continue
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Enter a number between 1 and 9.")
            continue

        board[pos] = "X"

        if check_winner("X"):
            print_board()
            print("🏆 You win!")
            break
        elif is_draw():
            print_board()
            print("🤝 It's a draw!")
            break

        ai_move()
        print_board()

        if check_winner("O"):
            print("💻 AI wins! Better luck next time.")
            break
        elif is_draw():
            print("🤝 It's a draw!")
            break

# ---------- Run ----------
if __name__ == "__main__":
    play_game()
