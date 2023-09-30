def getUserInput():
    dataNumerik = []

    while len(dataNumerik) < 20:
        try:
            userInput = int(
                input(f"Masukkan bilangan bulat ke-{len(dataNumerik )+1}\t: ")
            )

            if type(userInput) != int:
                raise Exception("Input harus berupa bilangan bulat!")

            genap = [x for x in dataNumerik if x % 2 == 0]
            genap.sort()

            ganjil = [x for x in dataNumerik if x % 2 == 1]
            ganjil.sort()

            dataNumerik.append(userInput)
            dataNumerik.sort()

        except Exception:
            print("Input harus berupa bilangan bulat!")

    return {"dataInput": dataNumerik, "ganjil": ganjil, "genap": genap}


data = getUserInput()

print(data["dataInput"])
print(f"Jumlah bilangan ganjil adalah\t: {len(data['ganjil'])}")
print(data["ganjil"])
print(f"Jumlah bilangan genap adalah\t: {len(data['genap'])}")
print(data["genap"])
