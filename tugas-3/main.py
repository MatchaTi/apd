# Nama : Adi Muhammad Syifai
# NIM : 2309106065
# Kelas : Informatika B23
from data import menu
import os


def clear_screen():
    os.system("clear")


def enter_continue():
    input("\nKlik enter untuk lanjut...")


clear_screen()


def quick_sort(arr, kind, filter_mod):
    if len(arr) <= 1:
        return arr
    else:
        kind = "harga" if kind == "harga" else "nama"
        pivot = arr[0]
        less = [item for item in arr[1:] if item[kind] <= pivot[kind]]
        greater = [item for item in arr[1:] if item[kind] > pivot[kind]]

        if filter_mod == "asc":
            return (
                quick_sort(less, kind, filter_mod)
                + [pivot]
                + quick_sort(greater, kind, filter_mod)
            )

        return (
            quick_sort(greater, kind, filter_mod)
            + [pivot]
            + quick_sort(less, kind, filter_mod)
        )


def cari_menu(keyword):
    hasil_pencarian = []

    for item in menu:
        if (
            keyword.lower() in item["kategori"].lower()
            or keyword.lower() in item["nama"].lower()
        ):
            hasil_pencarian.append(item)

    return hasil_pencarian


def sorting_data(data):
    while True:
        clear_screen()
        print("Sorting:\n")
        print("[1] Dari harga termurah ke harga termahal")
        print("[2] Dari harga termahal ke harga termurah")
        print("[3] Dari A - Z")
        print("[4] Dari Z - A")
        print("[5] Keluar\n")

        pilihan = input("Masukkan index menu: ")

        if pilihan == "1":
            asc = quick_sort(data, "harga", "asc")
            return asc
        elif pilihan == "2":
            desc = quick_sort(data, "harga", "desc")
            return desc
        elif pilihan == "3":
            asc = quick_sort(data, "nama", "asc")
            return asc
        elif pilihan == "4":
            desc = quick_sort(data, "nama", "desc")
            return desc
        elif pilihan == "5":
            return
        else:
            print(f"Pilihan tidak [{pilihan}] tersedia!")
            enter_continue()

        enter_continue()


def tampilkan_hasil(data):
    clear_screen()
    if data:
        for item in data:
            print(
                f"{item['nama']} {item['cto'] if 'cto' in item else ''} {'Ukuran ' + item['ukuran'] if 'ukuran' in item else ''} : {item['harga']}"
            )

        enter_continue()
        hasil = sorting_data(data)
        tampilkan_hasil(hasil)
    else:
        print("Tidak ada data!.")
        enter_continue()


def tampilkan_menu():
    while True:
        clear_screen()
        print("Menu:\n")
        print("[1] Makanan")
        print("[2] Minuman")
        print("[3] Keluar\n")

        pilihan = input("Masukkan index menu: ")

        if pilihan == "1":
            hasil_pencarian = cari_menu("makanan")
            tampilkan_hasil(hasil_pencarian)
        elif pilihan == "2":
            hasil_pencarian = cari_menu("minuman")
            tampilkan_hasil(hasil_pencarian)
        elif pilihan == "3":
            return
        else:
            print(f"Pilihan tidak [{pilihan}] tersedia!")
            enter_continue()


def main():
    while True:
        clear_screen()
        print("Menu:\n")
        print("[1] Tampilkan Menu")
        print("[2] Pencarian")
        print("[3] Keluar\n")

        pilihan = input("Masukkan index menu: ")

        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            input_user = input("Masukkan huruf atau kata kunci: ")
            hasil_pencarian = cari_menu(input_user)
            tampilkan_hasil(hasil_pencarian)
        elif pilihan == "3":
            return
        else:
            print(f"Pilihan tidak [{pilihan}] tersedia!")
            enter_continue()


print(len(menu))
main()
