import random

# Fungsi untuk mendapatkan pilihan pengguna
def get_user_choice():
    while True:
        user_choice = input("Masukkan pilihan Anda (Batu/Gunting/Kertas): ").strip().lower()
        if user_choice in ["batu", "gunting", "kertas"]:
            return user_choice
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk mendapatkan pilihan komputer
def get_computer_choice():
    return random.choice(["batu", "gunting", "kertas"])

# Fungsi untuk menentukan pemenang
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "batu" and computer_choice == "gunting") or \
         (user_choice == "gunting" and computer_choice == "kertas") or \
         (user_choice == "kertas" and computer_choice == "batu"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Fungsi utama
def main():
    print("Selamat datang di permainan Batu, Gunting, Kertas!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Anda memilih: {user_choice}")
        print(f"Komputer memilih: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Apakah Anda ingin bermain lagi? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Terima kasih telah bermain!")
            break

if __name__ == "__main__":
    main()
