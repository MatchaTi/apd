from menu import user_menu, main_menu
from auth import login, register
import os


admin = {
    "username": "admin",
    "password": "admin",
    "role": "admin",
}

list_users = ()
list_users = list(list_users)
databases = []
list_users.append(admin)


def main():
    while True:
        main_menu()

        choice = input("Pilih menu (1/2/3): ")

        if choice == "1":
            print(register(list_users))
        elif choice == "2":
            user = login(list_users)
            user_menu(user, databases, list_users)
        elif choice == "3":
            os.system("cls")
            print("Terima kasih! Sampai jumpa.")
            print("Program Selesai!")
            break
        else:
            os.system("cls")
            print(f"Pilihan {choice} tidak valid. Silakan pilih menu yang benar.")


if __name__ == "__main__":
    main()
