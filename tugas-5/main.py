import csv
import os

person = []

os.system("cls" if os.name == "nt" else "clear")

with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    print("Data sebelum diubah")
    for row in csv_reader:
        person.append(row)
        print(row)


with open("data.csv", mode="w") as csv_file:
    fieldnames = ["Nama_Karyawan", "Jam_Kerja", "Gaji_Pokok", "Gaji_Total"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    print("\nData setelah diubah")
    for data in person:
        jam_kerja = int(data["Jam_Kerja"])
        gaji_pokok = int(data["Gaji_Pokok"])
        gaji_total = int(data["Gaji_Total"])

        if jam_kerja > 40:
            jam_lembur = jam_kerja - 40
            gaji_total = (jam_kerja * gaji_pokok) + (jam_lembur * 100)
        else:
            gaji_total = jam_kerja * gaji_pokok

        data["Gaji_Total"] = gaji_total
        writer.writerow(data)
        print(data)
