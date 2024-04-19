import tkinter as tk
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def handle_click(row, col):
    global current_player, board_buttons, game_over
    
    if board[row][col] != " " or game_over:
        return
    
    board[row][col] = current_player
    board_buttons[row][col].config(text=current_player)
    
    winner = check_winner(board)
    if winner:
        status_label.config(text=f"Pemain {winner} menang!")
        game_over = True
        return

    if len(get_empty_cells(board)) == 0:
        status_label.config(text="Permainan seri!")
        game_over = True
        return
    
    current_player = "X" if current_player == "O" else "O"
    status_label.config(text=f"Giliran pemain {current_player}")

def restart_game():
    global current_player, board, board_buttons, game_over
    
    current_player = random.choice(["X", "O"])
    board = [[" " for _ in range(3)] for _ in range(3)]
    game_over = False
    
    for i in range(3):
        for j in range(3):
            board_buttons[i][j].config(text=" ", state="normal")
    
    status_label.config(text=f"Giliran pemain {current_player}")

root = tk.Tk()
root.title("Tic Tac Toe")

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = random.choice(["X", "O"])
game_over = False

board_buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        board_buttons[i][j] = tk.Button(root, text=" ", font=("Helvetica", 20), width=4, height=2,
                                        command=lambda row=i, col=j: handle_click(row, col))
        board_buttons[i][j].grid(row=i, column=j)
        
status_label = tk.Label(root, text=f"Giliran pemain {current_player}", font=("Helvetica", 12))
status_label.grid(row=3, columnspan=3)

restart_button = tk.Button(root, text="Restart", font=("Helvetica", 12), command=restart_game)
restart_button.grid(row=4, columnspan=3)

root.mainloop()
