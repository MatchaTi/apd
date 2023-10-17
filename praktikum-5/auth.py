import os


def admin_check(user):
    if user["role"] == "admin":
        return True

    return False


def login(users):
    try:
        username = input("Enter username\t: ")
        password = input("Enter password\t: ")

        user_exist = [
            x for x in users if x["username"] == username and x["password"] == password
        ]

        if len(user_exist) == 0:
            os.system("cls")
            raise Exception(
                f"Data {username} tidak ditemukan! Silahakan registrasi terlebih dahulu!"
            )

        os.system("cls")
        print("Berhasil login!")

        return user_exist[0]
    except Exception as e:
        print(e)
    except:
        print("Login Error")
        return


def register(users):
    username = input("Enter username\t: ")
    password = input("Enter password\t: ")

    user = {"username": username, "password": password, "role": "user"}

    users.append(user)
    return "Akun berhasil diregistrasi"


def show_user(list_users):
    users = [
        x for x in list_users if x["username"] != "admin" and x["password"] != "admin"
    ]

    print("[-] List Users")
    for x in range(len(users)):
        print(f"[{x + 1}] {users[x]['username']}")
