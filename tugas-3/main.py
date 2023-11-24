# Nama : Adi Muhammad Syifai
# NIM : 2309106065
# Kelas : Informatika B23
from data import menu
import os

os.system("clear")


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [item for item in arr[1:] if item["harga"] <= pivot["harga"]]
        greater = [item for item in arr[1:] if item["harga"] > pivot["harga"]]
        return quick_sort(less) + [pivot] + quick_sort(greater)
        # return quick_sort(greater) + [pivot] + quick_sort(less)


quick_sorted = menu.copy()
quick_sorted = quick_sort(quick_sorted)


def cari_menu(keyword):
    hasil_pencarian = []

    for item in quick_sorted:
        if (
            keyword.lower() in item["kategori"].lower()
            or keyword.lower() in item["nama"].lower()
        ):
            hasil_pencarian.append(item)

    return hasil_pencarian


input_user = input("Masukkan huruf atau kata kunci: ")

hasil_pencarian = cari_menu(input_user)

if hasil_pencarian:
    print("Hasil Pencarian:")
    for item in hasil_pencarian:
        print(
            f"{item['nama']} {item['cto'] if 'cto' in item else ''} {'Ukuran ' + item['ukuran'] if 'ukuran' in item else ''} : {item['harga']}"
        )
else:
    print("Tidak ada hasil yang ditemukan.")


def main():
    print("Hello")
