def getUserInput():
    dataNumerik = []
    genap = []
    ganjil = []

    while len(dataNumerik) < 20:
        try:
            userInput = int(input("Masukkan bilangan bulat\t: "))

            if type(userInput) != int:
                raise Exception("Input harus berupa bilangan bulat!")

            if userInput % 2 == 0:
                genap.append(userInput)
                genap.sort()
            else:
                ganjil.append(userInput)
                ganjil.sort()

            dataNumerik.append(userInput)

        except Exception:
            print("Input harus berupa bilangan bulat!")

    return {"dataInput": dataNumerik, "ganjil": ganjil, "genap": genap}


data = getUserInput()

print(data["dataInput"])
print(f"Jumlah bilangan ganjil adalah\t: {len(data['ganjil'])}")
print(data["ganjil"])
print(f"Jumlah bilangan genap adalah\t: {len(data['genap'])}")
print(data["genap"])
