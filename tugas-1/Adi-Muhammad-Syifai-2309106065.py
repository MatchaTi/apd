import os

print("| | _ | ||       ||   |    |       ||       ||  |_|  ||       |")
print("| | _ | ||       ||   |    |       ||       ||  |_|  ||       |")
print("| || || ||    ___||   |    |       ||   _   ||       ||    ___|")
print("|       ||   |___ |   |    |       ||  | |  ||       ||   |___ ")
print("|       ||    ___||   |___ |      _||  |_|  ||       ||    ___|")
print("|   _   ||   |___ |       ||     |_ |       || ||_|| ||   |___ ")
print("|__| |__||_______||_______||_______||_______||_|   |_||_______|")
print("\nNama\t: Adi Muhammad Syifai")
print("Kelas\t: Informatika B23")
print("NIM\t: 2309106065\n")

retry = "y"


def getUserInput():
    while True:
        try:
            x = int(input("Masukkan nilai Anda [0 - 100]: "))
            if x >= 0 and x <= 100:
                return x
            else:
                print("Nilai harus di dalam range 0 hingga 100!")
        except:
            print("Input harus berupa angka bilangan bulat!")


def checkValue(value):
    if value >= 90:
        return "A+"
    elif value >= 80:
        return "A-"
    elif value >= 75:
        return "B+"
    elif value >= 70:
        return "B-"
    elif value >= 65:
        return "C+"
    elif value >= 60:
        return "C-"
    elif value >= 50:
        return "D"
    else:
        return "E"


while retry != "n":
    try:
        x = getUserInput()
        print(checkValue(x))
        retry = input("Ingin mengulangi program? (y/n): ")
        os.system("cls")
    except KeyboardInterrupt:
        print("Anda telah membatalkan input.")

print("\nProgram Selesai!")
