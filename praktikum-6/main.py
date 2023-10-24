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
    print("====================")
    print("     Welcome to")
    print("    the Program")
    print("====================")
    while True:
        main_menu()

        choice = input("Choose menu (1/2/3): ")

        if choice == "1":
            print(register(list_users))
        elif choice == "2":
            user = login(list_users)
            if not user:
                print("Login failed")
            else:
                user_menu(user, databases, list_users)
        elif choice == "3":
            os.system("cls")
            print("The program has been finished")
            break
        else:
            os.system("cls")
            print(f"{choice} no match found!")


if __name__ == "__main__":
    main()
