import os
from crud import create_database, show_database, select_database, delete_database
from crud_db import crud_menu
from auth import show_user


def main_menu():
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Quit")


def display_menu(role):
    print("\nMenu:")
    print("1. Create database")
    print("2. Show database")
    print("3. Select database")
    print("4. Delete database")
    if role == "admin":
        print("5. Show all users")
        print("6. Logout")
    else:
        print("5. Logout")


def user_menu(user, databases, list_users):
    display_menu(user["role"])
    while True:
        choice = (
            input("Pilih menu (1/2/3/4/5/6): ")
            if user["role"] == "admin"
            else input("Pilih menu (1/2/3/4/5): ")
        )
        if choice == "1":
            os.system("cls")
            print(create_database(user, databases))
            display_menu(user["role"])
        elif choice == "2":
            os.system("cls")
            show_database(user, databases)
            display_menu(user["role"])
        elif choice == "3":
            os.system("cls")
            selected_db = select_database(user, databases)
            if selected_db:
                print(f"[-] Selected database {selected_db['name_database']}")
                crud_menu(selected_db)
            else:
                os.system("cls")
                print("No database selected")
            display_menu(user["role"])
        elif choice == "4":
            os.system("cls")
            delete_database(user, databases)
            display_menu(user["role"])
        elif choice == "5" and user["role"] == "admin":
            os.system("cls")
            show_user(list_users)
            display_menu(user["role"])
        elif choice == "5":
            os.system("cls")
            print("Berhasil logout")
            break
        elif choice == "6":
            print("6")
            os.system("cls")
            print("Berhasil logout")
            break
        else:
            os.system("cls")
            print(f"Pilihan {choice} tidak valid. Silakan pilih menu yang benar.")
