import os

print('| | _ | ||       ||   |    |       ||       ||  |_|  ||       |')
print('| | _ | ||       ||   |    |       ||       ||  |_|  ||       |')
print('| || || ||    ___||   |    |       ||   _   ||       ||    ___|')
print('|       ||   |___ |   |    |       ||  | |  ||       ||   |___ ')
print('|       ||    ___||   |___ |      _||  |_|  ||       ||    ___|')
print('|   _   ||   |___ |       ||     |_ |       || ||_|| ||   |___ ')
print('|__| |__||_______||_______||_______||_______||_|   |_||_______|')
print('\nNama\t: Adi Muhammad Syifai')
print('Kelas\t: Informatika B23')
print('NIM\t: 2309106065\n')

retry = 'y'

def circle():
    while True:
        try:
            r = float(input('Masukkan jari-jari\t\t\t: '))
            result = 3.14 * r**2

            os.system('cls')
            return f'Luas lingkaran dengan jari-jari {r} adalah {result}'
        except:
            print('Input jari-jari harus berupa angka!')

def triangle():
    while True:
        try:
            a = float(input('Masukkan alas\t\t\t\t: '))
            t = float(input('Masukkan tinggi\t\t\t\t: '))
            result = 1/2 * a * t

            os.system('cls')
            return f'Luas segitiga dengan alas {a} dan tinggi {t} adalah {result}'
        except:
            print('Input alas/tinggi harus berupa angka!')

def chooseProgram():
    while True:
        userChoice = input('Tentukan pilihan untuk menghitung luas\t:\nLingkaran[l] / Segitiga[s]\t\t: ')

        if userChoice == 'l':
            return circle()
        elif userChoice == 's':
           return triangle() 
        else:
            os.system('cls')
            print(f'Pilihan {userChoice} tidak tersedia!')

while retry != 'n':
    print(chooseProgram())
    retry = input('Ingin mengulangi program? (y/n)\t\t: ')
    os.system('cls')

print('Program Selesai!')