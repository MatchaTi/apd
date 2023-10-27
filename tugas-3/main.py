# Nama : Adi Muhammad Syifai
# NIM : 2309106065
# Kelas : Informatika B23

# Data kuliner dalam bentuk list
kuliner = [
    {"nama": "Mie Ayam", "harga": 25000},
    {"nama": "Nasi Goreng", "harga": 22000},
    {"nama": "Sate Padang", "harga": 30000},
    {"nama": "Bakso Malang", "harga": 18000},
    {"nama": "Rendang", "harga": 35000}
]

# Implementasi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # Bandingkan harga dua item yang berdekatan
            if arr[j]["harga"] > arr[j + 1]["harga"]:
                # Jika harga item pertama lebih besar, tukar posisi item
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Implementasi Quick Sort
def quick_sort(arr):
    # Jika daftar memiliki satu item atau kurang, sudah terurut
    if len(arr) <= 1:
        return arr
    else:
        # Pilih pivot (biasanya elemen pertama) untuk membagi data
        pivot = arr[0]
        # Bagi data menjadi dua bagian: yang lebih kecil atau sama dengan pivot dan yang lebih besar
        less = [item for item in arr[1:] if item["harga"] <= pivot["harga"]]
        greater = [item for item in arr[1:] if item["harga"] > pivot["harga"]]
        # Gabungkan dua bagian yang diurutkan bersama dengan pivot di tengah
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Panggil algoritma pengurutan yang diinginkan
bubble_sorted = kuliner.copy()
bubble_sort(bubble_sorted)

quick_sorted = kuliner.copy()
quick_sorted = quick_sort(quick_sorted)

# Tampilkan hasil pengurutan
print("Bubble Sort:")
for item in bubble_sorted:
    print(f"{item['nama']}: Rp {item['harga']}")

print("\nQuick Sort:")
for item in quick_sorted:
    print(f"{item['nama']}: Rp {item['harga']}")
