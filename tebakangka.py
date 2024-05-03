import random
import math

# Algoritma Minimax dengan Alpha-Beta Pruning
def minimax(number, depth, maximizing_player, alpha, beta):
    if depth == 0:
        return number

    if maximizing_player:
        max_eval = -math.inf
        for guess in range(1, 101):
            eval = minimax(number, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for guess in range(1, 101):
            eval = minimax(number, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Fungsi untuk menebak angka oleh komputer (pemain1)
def ai_guess(number):
    best_guess = None
    best_eval = -math.inf
    alpha = -math.inf
    beta = math.inf
    for guess in range(1, 101):
        eval = minimax(number, 3, False, alpha, beta)  # Depth ditetapkan di sini
        if eval > best_eval:
            best_eval = eval
            best_guess = guess
    return best_guess

# Fungsi untuk pemain manusia (pemain2)
def player_guess():
    while True:
        guess = input("Tebak angka antara 1 dan 100: ")
        if guess.isdigit() and 1 <= int(guess) <= 100:
            return int(guess)
        else:
            print("Masukan tidak valid! Harap masukkan angka antara 1 dan 100.")

# Fungsi utama permainan
def main():
    number = random.randint(1, 100)
    print("Komputer telah memilih sebuah angka antara 1 dan 100. Tebak angka tersebut!")

    attempts = 0
    while True:
        guess = player_guess()
        attempts += 1
        if guess < number:
            print("Angka terlalu rendah. Coba lagi!")
        elif guess > number:
            print("Angka terlalu tinggi. Coba lagi!")
        else:
            print(f"Selamat! Anda menebak angka ({number}) dengan benar dalam {attempts} percobaan.")
            break

    print("\nSekarang, mari komputer yang menebak angka yang Anda pilih.")
    number = player_guess()
    guess = ai_guess(number)
    print(f"Komputer menebak angka: {guess}")
    print("Tunggu sebentar...")
    print("Komputer sedang memproses...")
    print("...")
    print(f"Komputer menebak angka {guess}.")
    if guess == number:
        print("Komputer menebak dengan benar!")
    else:
        print("Komputer menebak salah.")

if __name__ == "__main__":
    main()
