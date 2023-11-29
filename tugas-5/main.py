import csv

person = []

with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    for row in csv_reader:
        person.append(row)


with open("data.csv", mode="w") as csv_file:
    fieldnames = ["Nama_Karyawan", "Jam_Kerja", "Gaji_Pokok", "Gaji_Total"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for data in person:
        jam_kerja = int(data["Jam_Kerja"])
        gaji_pokok = int(data["Gaji_Pokok"])
        gaji_total = int(data["Gaji_Total"])

        if jam_kerja > 40:
            jam_lembur = jam_kerja - 40
            gaji_total = (jam_kerja * gaji_pokok) + (jam_lembur * 100)
        else:
            gaji_total = jam_kerja * gaji_pokok

        writer.writerow(
            {
                "Nama_Karyawan": data["Nama_Karyawan"],
                "Jam_Kerja": data["Jam_Kerja"],
                "Gaji_Pokok": data["Gaji_Pokok"],
                "Gaji_Total": gaji_total,
            }
        )
