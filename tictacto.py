import pygame
import math
import random

# Inisialisasi Pygame
pygame.init()

# Variabel global
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
WIN_FONT = pygame.font.Font(None, 50)

# Membuat layar permainan
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Membuat papan permainan
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Fungsi untuk menggambar garis papan permainan
def draw_lines():
    # Garis horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Garis vertikal
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Fungsi untuk menggambar simbol X atau O di kotak tertentu
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

# Fungsi untuk menandai kotak yang dipilih oleh pemain
def mark_square(row, col, player):
    board[row][col] = player

# Fungsi untuk memeriksa apakah terdapat pemenang
def winner(board, player):
    # Mengecek baris
    for row in range(BOARD_ROWS):
        if all([board[row][col] == player for col in range(BOARD_COLS)]):
            return True
    # Mengecek kolom
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):
            return True
    # Mengecek diagonal
    if all([board[i][i] == player for i in range(BOARD_ROWS)]):
        return True
    if all([board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)]):
        return True
    return False

# Fungsi untuk mengecek apakah terdapat kotak kosong di papan permainan
def empty_squares(board):
    return any([board[row][col] == ' ' for row in range(BOARD_ROWS) for col in range(BOARD_COLS)])

# Fungsi untuk menampilkan pesan hasil permainan
def display_result(winner):
    result_text = "It's a Tie!" if winner == 'Tie' else f"{winner} wins!"
    text_surface = WIN_FONT.render(result_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

# Fungsi untuk mengevaluasi papan dengan algoritma Minimax dengan pruning alpha-beta
def minimax(board, depth, maximizing_player, alpha, beta):
    if winner(board, 'X'):
        return -1
    elif winner(board, 'O'):
        return 1
    elif not empty_squares(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Fungsi untuk memilih langkah terbaik menggunakan algoritma Minimax dengan pruning alpha-beta
def best_move(board):
    best_score = -math.inf
    best_move = None
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

# Fungsi utama permainan
def main():
    current_player = 'X'
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                break
            if event.type == pygame.MOUSEBUTTONDOWN and current_player == 'X' and not game_over:
                mouseX = event.pos[0] // SQUARE_SIZE
                mouseY = event.pos[1] // SQUARE_SIZE
                if board[mouseY][mouseX] == ' ':
                    mark_square(mouseY, mouseX, current_player)
                    if winner(board, current_player):
                        display_result(current_player)
                        game_over = True
                    elif not empty_squares(board):
                        display_result('Tie')
                        game_over = True
                    current_player = 'O'
            elif current_player == 'O' and not game_over:
                move = best_move(board)
                mark_square(move[0], move[1], current_player)
                if winner(board, current_player):
                    display_result(current_player)
                    game_over = True
                elif not empty_squares(board):
                    display_result('Tie')
                    game_over = True
                current_player = 'X'

        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()
        pygame.display.flip()

    pygame.time.wait(3000)
    pygame.quit()

if __name__ == '__main__':
    main()
