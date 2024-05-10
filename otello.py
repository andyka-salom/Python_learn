import math

# Definisi simbol
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2

# Ukuran papan
ROWS = 6
COLS = 7

# Fungsi untuk mengecek apakah terdapat pemenang
def check_winner(board, player):
    # Mengecek horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == player:
                return True

    # Mengecek vertikal
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == player:
                return True

    # Mengecek diagonal miring ke kanan atas
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == player:
                return True

    # Mengecek diagonal miring ke kiri atas
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] == player:
                return True

    return False

# Fungsi untuk mengecek apakah terdapat celah kosong untuk memasukkan koin
def is_valid_location(board, col):
    return board[ROWS - 1][col] == EMPTY

# Fungsi untuk mendapatkan baris terbawah yang kosong pada kolom tertentu
def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == EMPTY:
            return r

# Algoritma Alpha-Beta Pruning
def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for col in range(COLS):
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                board[row][col] = PLAYER1
                eval = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
                board[row][col] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for col in range(COLS):
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                board[row][col] = PLAYER2
                eval = alpha_beta_pruning(board, depth - 1, alpha, beta, True)
                board[row][col] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Fungsi evaluasi untuk menentukan skor papan
def evaluate(board):
    if check_winner(board, PLAYER1):
        return 100
    elif check_winner(board, PLAYER2):
        return -100
    else:
        return 0

# Fungsi untuk mengecek apakah permainan sudah selesai
def game_over(board):
    return check_winner(board, PLAYER1) or check_winner(board, PLAYER2) or is_board_full(board)

# Fungsi untuk mengecek apakah papan penuh
def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLS))

# Fungsi untuk membuat papan baru
def create_board():
    return [[EMPTY] * COLS for _ in range(ROWS)]

# Fungsi untuk mencetak papan
def print_board(board):
    for row in board:
        print(row)

# Fungsi utama permainan
def main():
    board = create_board()

    while not game_over(board):
        print_board(board)
        col = int(input("Player 1, choose a column (0-6): "))
        while not is_valid_location(board, col):
            print("Column is full. Choose another column.")
            col = int(input("Player 1, choose a column (0-6): "))
        row = get_next_open_row(board, col)
        board[row][col] = PLAYER1

        if game_over(board):
            break

        print_board(board)
        col = alpha_beta_pruning(board, 5, -math.inf, math.inf, True)
        row = get_next_open_row(board, col)
        board[row][col] = PLAYER2

    print_board(board)
    if check_winner(board, PLAYER1):
        print("Player 1 wins!")
    elif check_winner(board, PLAYER2):
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
