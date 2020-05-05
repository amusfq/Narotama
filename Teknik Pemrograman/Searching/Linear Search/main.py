import time
import os

def search(arr, x):
    for i in range(0, len(arr)):
        if (arr[i] == x):
            return i
    return -1
def linear():
    while True:
        os.system('clear')
        print("=============================")
        print("        Linear Search        ")
        print("=============================")
        print("Masukkan array angka")
        print('(pisahkan dengan koma)')
        inp = input()
        if inp.replace(',', '').isnumeric():
            inp = inp.split(',')
            print('Data array anda: {}' .format(inp))
            x = input('Masukkan angka yang dicari: ')
            if x.isnumeric():
                start = time.time()
                result = search(inp, x)
                end = time.time()
                if result == -1:
                    print("Data yang dicari tidak ada di array")
                else:
                    print("Data yang dicari ada di array ke-{}" .format(result))
                print()
                print("Program selesai dalam %f detik" % (end - start))
                input("(Enter untuk melanjutkan)")
                return False
            else:
                print("Target anda bukan angka")
                input("(Enter untuk melanjutkan)")
        else:
            print("Array anda bPILIH ALGORITMA SORTINGukan angka")
            input("(Enter untuk melanjutkan)")

while True:
    os.system('clear')
    print("=============================")
    print("=       Linear Search       =")
    print("=                           =")
    print("=  1. Mulai cari            =")
    print("=  2. Exit                  =")
    print("=                           =")
    print("=============================")
    pil = int(input("Masukkan pilihan: "))
    if pil == 1 :
        linear()
    elif pil == 2:
        exit()
    else:
        os.system('clear')
        print("Pilihan salah..")
        input("(Enter untuk melanjutkan)")