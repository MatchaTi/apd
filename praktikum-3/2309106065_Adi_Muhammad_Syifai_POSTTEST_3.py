import os

retry = "y"

os.system("cls")

print("Nama\t: Adi Muhammad Syifai")
print("NIM\t: 2309106065")
print("Kelas\t: Informatika B23")
print("Post Test 3 Praktikum")
print("Program Menentukan Tahun Kabisat\n")


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


while retry != "n":
    print(checkLeapYear())
    retry = input("Ingin mengulang program? (y/n)\t: ").lower()
    os.system("cls")

print("Program Selesai!")
