import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ukuran layar
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Font
FONT = pygame.font.Font(None, 48)

# Daftar kata untuk ditebak
words = ["apple", "banana", "orange", "grape", "pineapple", "strawberry", "watermelon", "kiwi", "peach", "mango"]

# Fungsi untuk memilih kata secara acak
def choose_word():
    return random.choice(words)

# Fungsi untuk menebak huruf oleh pemain (pemain2)
def player_guess():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key in (pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z):
                    return chr(event.key)

# Fungsi untuk menggambar hangman
def draw_hangman(stage):
    parts = ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"]
    colors = [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]

    if stage > 0:
        pygame.draw.circle(SCREEN, colors[0], (400, 150), 30)
    if stage > 1:
        pygame.draw.line(SCREEN, colors[1], (400, 180), (400, 330), 4)
    if stage > 2:
        pygame.draw.line(SCREEN, colors[2], (400, 210), (350, 260), 4)
    if stage > 3:
        pygame.draw.line(SCREEN, colors[3], (400, 210), (450, 260), 4)
    if stage > 4:
        pygame.draw.line(SCREEN, colors[4], (400, 330), (350, 400), 4)
    if stage > 5:
        pygame.draw.line(SCREEN, colors[5], (400, 330), (450, 400), 4)

# Fungsi utama permainan
def main():
    word = choose_word()
    guesses = ["_" for _ in word]
    stage = 0

    clock = pygame.time.Clock()

    while True:
        SCREEN.fill(WHITE)
        draw_hangman(stage)

        text = FONT.render(" ".join(guesses), True, BLACK)
        SCREEN.blit(text, (300, 500))

        pygame.display.update()

        guess = player_guess()

        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    guesses[i] = guess
        else:
            stage += 1

        if "_" not in guesses or stage == 6:
            break

        clock.tick(30)

    if "_" not in guesses:
        text = FONT.render("Selamat! Anda berhasil menebak kata: " + word, True, BLACK)
    else:
        text = FONT.render("Maaf! Anda kalah. Kata yang benar adalah: " + word, True, BLACK)

    SCREEN.blit(text, (100, 200))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()
