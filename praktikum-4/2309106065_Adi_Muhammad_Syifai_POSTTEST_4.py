import os

retry = "y"
listUsers = []

os.system("cls")

print("Nama\t: Adi Muhammad Syifai")
print("NIM\t: 2309106065")
print("Kelas\t: Informatika B23")
print("Post Test 3 Praktikum")
print("Program Menentukan Tahun Kabisat\n")


def login():
    counter = 1
    while counter <= 3:
        try:
            name = str(input("Masukkan nama Anda\t: "))
            password = int(input("Masukkan password Anda\t: "))

            person = {"name": name, "password": password}

            if person not in listUsers and counter != 3:
                counter += 1
                os.system("cls")
                raise Exception(
                    f"Data {person['name']} tidak ditemukan! Silahakan registrasi terlebih dahulu!"
                )
            elif counter == 3:
                os.system("cls")
                print("Kesempatan login anda sudah habis!")
                break

            os.system("cls")
            print("Berhasil login!")
            print(checkLeapYear())

            return
        except ValueError:
            print("Masukkan data input yang valid!")
        except Exception as e:
            print(e)
        except:
            print("Login Error")
            return


def register():
    while True:
        try:
            name = str(input("Masukkan nama Anda\t: "))
            password = int(input("Masukkan password Anda\t: "))

            person = {"name": name, "password": password}

            listUsers.append(person)

            os.system("cls")
            print("Akun berhasil diregistrasi!")
            return
        except ValueError:
            os.system("cls")
            print("Masukkan data input yang valid!")
        except:
            os.system("cls")
            print("Register Error")


def checkLeapYear():
    while True:
        try:
            userInput = int(input("Masukkan tahun\t: "))

            if userInput < 0:
                raise Exception("Angka tahun tidak boleh minus!")

            if (userInput % 4 == 0 and userInput % 100 != 0) or userInput % 400 == 0:
                return f"{userInput} adalah tahun kabisat"

            return f"{userInput} bukan tahun kabisat"

        except ValueError:
            os.system("cls")
            print("Inputan harus berupa angka bilangan bulat (tahun)!")
        except Exception as e:
            os.system("cls")
            print(e)


def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        choice = input("Pilih menu (1/2/3): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
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
