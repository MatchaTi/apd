# Nama : Adi Muhammad Syifai
# NIM : 2309106065
# Kelas : Informatika B23
from data import menu
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def enter_continue():
    input("\nKlik enter untuk lanjut...")


clear_screen()

pesanan = []


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


def print_list(data):
    for i, item in enumerate(data):
        item_name = item["nama"]
        cto = item.get("cto", "")
        ukuran = f"Ukuran {item['ukuran']}" if "ukuran" in item else ""
        harga = item["harga"]
        ammount = f"({item['amount']})" if "amount" in item else ""
        print(f"{i+1}. {item_name} {cto} {ukuran} Rp. {harga} {ammount}")


def pesan_menu(menu):
    while True:
        try:
            nomor = int(input("Pilih nomor menu yang ingin dipesan (0 untuk keluar): "))

            if nomor >= 1 and nomor <= len(menu):
                item = menu[nomor - 1]
                if item in pesanan:
                    index = pesanan.index(item)
                    pesanan[index]["amount"] += 1
                else:
                    item["amount"] = 1
                    pesanan.append(item)

                print(f"{item['nama']} telah ditambahkan ke dalam pesanan.")
                enter_continue()
            elif nomor == 0:
                return
            else:
                print("Nomor menu tidak valid.")
        except ValueError:
            print("Nomor menu tidak valid.")


def cari_menu(keyword):
    hasil_pencarian = []

    for item in menu:
        if (
            keyword.lower() in item["kategori"].lower()
            or keyword.lower() in item["nama"].lower()
        ):
            hasil_pencarian.append(item)

    return hasil_pencarian


def tampilkan_hasil(data):
    clear_screen()
    if data:
        print_list(data)
        enter_continue()
        pesan_menu(data)
    else:
        print("Tidak ada data!.")
        enter_continue()


def sorting_data():
    hasil_pencarian = []
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

        clear_screen()
        print("Sorting:\n")
        print("[1] Dari harga termurah ke harga termahal")
        print("[2] Dari harga termahal ke harga termurah")
        print("[3] Dari A - Z")
        print("[4] Dari Z - A")
        print("[5] Keluar\n")

        pilihan = input("Masukkan index menu: ")

        if pilihan == "1":
            asc = quick_sort(hasil_pencarian, "harga", "asc")
            tampilkan_hasil(asc)
            return
        elif pilihan == "2":
            desc = quick_sort(hasil_pencarian, "harga", "desc")
            tampilkan_hasil(desc)
            return
        elif pilihan == "3":
            asc = quick_sort(hasil_pencarian, "nama", "asc")
            tampilkan_hasil(asc)
            return
        elif pilihan == "4":
            desc = quick_sort(hasil_pencarian, "nama", "desc")
            tampilkan_hasil(desc)
            return
        elif pilihan == "5":
            return
        else:
            print(f"Pilihan tidak [{pilihan}] tersedia!")
            enter_continue()

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


def edit_pesanan():
    while True:
        try:
            nomor = int(
                input("Pilih nomor pesanan yang ingin diubah (0 untuk keluar): ")
            )

            if nomor >= 1 and nomor <= len(pesanan):
                item = pesanan[nomor - 1]
                amount = int(input("Masukkan jumlah pesanan: "))
                item["amount"] = amount
                print(f'Jumlah pesanan {item["nama"]} telah diubah menjadi {amount}.')
                enter_continue()
            elif nomor == 0:
                break
            else:
                print("Nomor pesanan tidak valid.")
        except ValueError:
            print("Nomor pesanan tidak valid.")


def hapus_pesanan():
    while True:
        try:
            nomor = int(
                input("Pilih nomor pesanan yang ingin dihapus (0 untuk keluar): ")
            )

            if nomor >= 1 and nomor <= len(pesanan):
                item = pesanan[nomor - 1]
                pesanan.remove(item)
                print(f'Pesanan {item["nama"]} telah dihapus.')
                enter_continue()
            elif nomor == 0:
                break
            else:
                print("Nomor pesanan tidak valid.")
        except ValueError:
            print("Nomor pesanan tidak valid.")


def keranjang():
    clear_screen()
    print("Keranjang:\n")
    if pesanan:
        print_list(pesanan)
        print("\nMenu:\n")
        print("[1] Edit jumlah pesanan")
        print("[2] Hapus pesanan")
        print("[3] Bayar\n")

        while True:
            pilihan = input("Masukkan index menu: ")

            if pilihan == "1":
                edit_pesanan()
            elif pilihan == "2":
                hapus_pesanan()
            elif pilihan == "3":
                total = 0
                for item in pesanan:
                    total += item["harga"] * item["amount"]
                print(f"Total harga yang harus dibayar adalah Rp. {total}.")
                enter_continue()
                print("Berhasil bayar! Terima kasih telah berbelanja.")
                enter_continue()
                pesanan.clear()
                return
            else:
                print(f"Pilihan tidak [{pilihan}] tersedia!")
    else:
        print("Keranjang kosong!")
    enter_continue()


def main():
    while True:
        clear_screen()
        print("Menu:\n")
        print("[1] Tampilkan Menu")
        print("[2] Pencarian")
        print("[3] Sorting")
        print("[4] Keranjang")
        print("[5] Keluar\n")

        pilihan = input("Masukkan index menu: ")

        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            input_user = input("Masukkan huruf atau kata kunci: ")
            hasil_pencarian = cari_menu(input_user)
            tampilkan_hasil(hasil_pencarian)
        elif pilihan == "3":
            sorting_data()
        elif pilihan == "4":
            keranjang()
        elif pilihan == "5":
            return
        else:
            print(f"Pilihan tidak [{pilihan}] tersedia!")
            enter_continue()


main()
