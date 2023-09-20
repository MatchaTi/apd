import os


def catalog():
    print("====================")
    print("   Selamat Datang")
    print("  Di Kumala Market")
    print("====================\n")
    print("1. Buku Sejarah\t: Rp.50.000")
    print("2. Buku Novel\t: Rp.40.000")
    print("3. Manga\t: Rp.25.000")
    print("4. Manhwa\t: Rp.30.000")
    print("5. Bayar")


harga = {
    "1": 50000,
    "2": 40000,
    "3": 25000,
    "4": 30000,
}

jumlahBeli = 0
jumlahBuku = 0
total = 0
retry = "y"


def getUserInput():
    pilihan = ""

    while pilihan != "5":
        pilihan = input("Masukkan nomor index buku yang ingin dibeli\t: ")

        if pilihan in harga:
            return pilihan
        elif pilihan == "5":
            return pilihan
        else:
            print(f"Pilihan {pilihan} tidak tersedia!")


while retry != "n":
    catalog()
    jumlahBeli = 0
    jumlahBuku = 0
    total = 0

    while True:
        pilihan = getUserInput()

        if pilihan == "5":
            break

        jumlahBeli = int(input("Masukkan jumlah buku yang ingin dibeli\t\t: "))
        jumlahBuku += jumlahBeli
        total += harga[pilihan] * jumlahBeli

    print("====================")
    print("   Terima Kasih")
    print(" Telah berbelanja")
    print("  Di Kumala Market")
    print("====================")

    if jumlahBuku >= 5 and total >= 100000:
        print(f"Total belanja dengan diskon 20% : {(total - (total * 20) / 100)}")
    else:
        print(f"Total belanja : {total}")

    retry = input("Ingin mengulangi program? (y/n)\t: ").lower()
    os.system("cls")

os.system("cls")
print("====================")
print("  Program Selesai")
print("====================")
