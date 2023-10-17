def create_database(user, databases):
    name_database = input("Database Name\t\t: ")
    new_database = {
        "name_database": name_database,
        "username": user["username"],
        "data": [],
    }

    databases.append(new_database)

    return "Database created successfully!"


def show_database(user, databases):
    print("[-] List databases")
    if user["role"] == "admin":
        if len(databases) == 0:
            print("No databases")
        else:
            for i in range(len(databases)):
                print(f"[{i + 1}] {databases[i]['name_database']}")
    else:
        user_databases = [db for db in databases if db["username"] == user["username"]]
        if len(user_databases) == 0:
            print("No databases")
        else:
            for i in range(len(user_databases)):
                print(f"[{i + 1}] {user_databases[i]['name_database']}")


def select_database(user, databases):
    show_database(user, databases)
    try:
        index_db = int(input("Choose a database to select (enter the index): "))

        if user["role"] == "admin":
            if 1 <= index_db <= len(databases):
                selected = databases[index_db - 1]

                return selected
            else:
                print("Invalid database index. No database found.")
        else:
            user_databases = [
                db for db in databases if db["username"] == user["username"]
            ]
            if 1 <= index_db <= len(user_databases):
                selected = user_databases[index_db - 1]

                return selected
            else:
                print("Invalid database index. No database found.")
    except (ValueError, IndexError):
        print("Invalid input or database index. No database found.")


def delete_database(user, databases):
    show_database(user, databases)
    try:
        index_db = int(input("Choose a database to delete (enter the index): "))

        if user["role"] == "admin":
            if 1 <= index_db <= len(databases):
                deleted_db = databases.pop(index_db - 1)
                print(f"Database '{deleted_db['name_database']}' has been deleted.")
            else:
                print("Invalid database index. No database deleted.")
        else:
            user_databases = [
                db for db in databases if db["username"] == user["username"]
            ]
            if 1 <= index_db <= len(user_databases):
                deleted_db = user_databases.pop(index_db - 1)
                print(f"Database '{deleted_db['name_database']}' has been deleted.")
            else:
                print("Invalid database index. No database deleted.")
    except (ValueError, IndexError):
        print("Invalid input or database index. No database deleted.")
