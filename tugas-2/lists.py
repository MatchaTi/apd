def getUserInput():
    dataNumerik = []
    genap = []
    ganjil = []

    while len(dataNumerik) < 20:
        try:
            print(len(dataNumerik), "length panjang")
            userInput = int(input("Masukkan bilangan bulat\t: "))

            if type(userInput) != int:
                raise Exception("Input harus berupa bilangan bulat!")

            if userInput % 2 == 0:
                genap.append(userInput)
            else:
                ganjil.append(userInput)

            dataNumerik.append(userInput)

        except Exception:
            print("Input harus berupa bilangan bulat!")

    return {"dataInput": dataNumerik, "ganjil": ganjil, "genap": genap}


data = getUserInput()

print(data["dataInput"])
print(data["ganjil"])
print(data["genap"])
