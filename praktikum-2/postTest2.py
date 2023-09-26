import os


retry = "y"


def getUserInput():
    while True:
        try:
            nama = str(input("Masukkan nama mahasiswa\t\t: "))
            nim = int(input("Masukkan NIM mahasiswa\t\t: "))

            nim = str(nim)

            if len(nim) != 10:
                raise Exception("NIM harus 10 digit!")

            nim = int(nim)

            umur = int(input("Masukkan umur mahasiswa\t\t: "))
            tinggiBadan = float(input("Masukkan tinggi badan mahasiswa\t: "))
            moduloNIM = (nim % 1000) % 7

            return {
                "intro": f"Hi! Nama saya {nama} dengan NIM {nim}, saya berumur {umur} tahun dan memiliki tinggi {tinggiBadan} cm",
                "moduloNIM": f"3 angka terakhir NIM saya {nim} dimodulus 7 adalah {moduloNIM}",
            }
        except Exception as e:
            print(f"NIM harus 10 digit!")
        except:
            print("Masukkan data yang valid!")


while retry != "n":
    userInput = getUserInput()
    print(userInput["intro"])
    print(userInput["moduloNIM"])
    retry = input("Ingin mengulang program? (y/n)\t: ").lower()
    os.system("cls")

print("Program Selesai!")
