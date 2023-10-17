import os


def display_db_menu():
    print("\nMenu:")
    print("1. Show data")
    print("2. Insert data")
    print("3. Update data")
    print("4. Delete data")
    print("5. Quit")


def show_data(data):
    if not data:
        print("[-] No data")
    else:
        print("[-] List Data")
        for d in range(len(data)):
            print(f"[{d +1}] {data[d]}")


def insert_data(data):
    new_data = input("Insert data\t: ")

    data.append(new_data)

    print("Inserted data")


def update_data(data):
    show_data(data)
    if data:
        index_data = int(input("Choose a data to update (enter the index): "))
        new_data = input("enter the new data: ")
        data[index_data - 1] = new_data
        print("Data updated")


def delete_data(data):
    show_data(data)
    if data:
        index_data = int(input("Choose a data to delete (enter the index): "))
        deleted_data = data.pop(index_data - 1)
        print(f"Database '{deleted_data}' has been deleted.")


def crud_menu(database):
    display_db_menu()
    while True:
        choice = input("Select action\t: ")

        if choice == "1":
            os.system("cls")
            show_data(database["data"])
            display_db_menu()
        elif choice == "2":
            os.system("cls")
            insert_data(database["data"])
            display_db_menu()
        elif choice == "3":
            os.system("cls")
            update_data(database["data"])
            display_db_menu()
        elif choice == "4":
            os.system("cls")
            delete_data(database["data"])
            display_db_menu()
        elif choice == "5":
            os.system("cls")
            break
        else:
            print(f"{choice} is not a valid choice")
