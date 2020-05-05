import time
import os

def linear(arr, x):
    for i in range(0, len(arr)):
        if (arr[i] == x):
            return i
    return -1

def binSearch(array, target):
    min = 0
    max = len(array) - 1
    while min <= max:
        tengah = min + (max - min) // 2
        if array[tengah] == target:
            return tengah
        elif array[tengah] < target:
            min = tengah + 1
        else:
            max = tengah - 1
    return -1

def compare():
    while True:
        os.system('clear')
        print("=============================")
        print("=     Comparison Search     =")
        print("=============================")
        print("Masukkan array angka")
        print('(pisahkan dengan koma)')
        inp = input()
        if inp.replace(',', '').isnumeric():
            inp = inp.split(',')
            print('Data array anda: {}' .format(inp))
            x = input('Masukkan angka yang dicari: ')
            if x.isnumeric():
                print()
                start = time.time()
                result = linear(inp, x)
                end = time.time()
                if result == -1:
                    print("Hasil linear search : tidak ditemukan")
                else:
                    print("Hasil linear search : ada di array ke-{}" .format(result))
                print("Ditemukan dalam %f detik" % (end - start))
                print()
                start = time.time()
                result = binSearch(inp, x)
                end = time.time()

                if result == -1:
                    print("Hasil binary search : tidak ditemukan")
                else:
                    print("Hasil binary search : ada di array ke-{}" .format(result))
                print("Ditemukan dalam %f detik" % (end - start))

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
    print("=     Comparison Search     =")
    print("=                           =")
    print("=  1. Mulai perbandingan    =")
    print("=  2. Exit                  =")
    print("=                           =")
    print("=============================")
    pil = int(input("Masukkan pilihan: "))
    if pil == 1 :
        compare()
    elif pil == 2:
        exit()
    else:
        os.system('clear')
        print("Pilihan salah..")
        input("(Enter untuk melanjutkan)")