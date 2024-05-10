import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Konstanta
WIDTH, HEIGHT = 300, 300
TILE_SIZE = WIDTH // 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Fungsi untuk menggambar teks di tengah tile
def draw_text(surface, text, color, rect):
    font_surface = FONT.render(text, True, color)
    font_rect = font_surface.get_rect(center=rect.center)
    surface.blit(font_surface, font_rect)

# Fungsi untuk membuat permainan baru
def new_game():
    nums = list(range(1, 9))
    random.shuffle(nums)
    nums.append(0)  # Tambahkan slot kosong
    return nums

# Fungsi untuk mengecek apakah permainan selesai
def is_game_over(board):
    return board[:-1] == sorted(board[:-1])

# Fungsi untuk menggambar papan permainan
def draw_board(screen, board):
    for i in range(3):
        for j in range(3):
            num = board[i * 3 + j]
            if num == 0:
                pygame.draw.rect(screen, BLACK, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                draw_text(screen, str(num), BLACK, pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Fungsi untuk mencari posisi mouse yang diklik
def get_clicked_pos(pos):
    x, y = pos
    row = y // TILE_SIZE
    col = x // TILE_SIZE
    return row, col

# Fungsi utama
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("8 Puzzle")

    board = new_game()
    running = True

    while running:
        screen.fill(BLACK)
        draw_board(screen, board)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_clicked_pos(pygame.mouse.get_pos())
                empty_row, empty_col = divmod(board.index(0), 3)

                # Mengecek apakah kotak yang diklik bersebelahan dengan kotak kosong
                if (abs(row - empty_row) == 1 and col == empty_col) or (abs(col - empty_col) == 1 and row == empty_row):
                    clicked_index = row * 3 + col
                    empty_index = empty_row * 3 + empty_col
                    board[clicked_index], board[empty_index] = board[empty_index], board[clicked_index]

                    # Mengecek apakah permainan selesai
                    if is_game_over(board):
                        print("Congratulations! You've solved the puzzle!")
                        running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
