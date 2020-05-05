import time
import os

def start():
    while True:
        os.system('clear')
        print("========================================")
        print("             BILANGAN ARRAY             ")
        print(" [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]")
        print("                                        ")
        print("   Masukkan Bilangan Yang Akan Dicari   ")
        print("                                        ")
        print("========================================")
        arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        x = input()
        if x.isnumeric():
            def binSearch(array, target):
                min = 0
                max = len(array) - 1
                while min <= max:
                    tengah = min + (max - min) // 2
                    if int(array[tengah]) == target:
                        return tengah
                    elif int(array[tengah]) < target:
                        min = tengah + 1
                    else:
                        max = tengah - 1
                return -1

            start = time.time()
            hasil = binSearch(arr, int(x))
            end = time.time()

            if hasil != -1:
                print("Bilangan {} ada di array index ke {}" .format(x, hasil))
            else:
                print("Bilangan {} tidak ada didalam array" .format(x))

            print("Selesai dalam %f detik" % (end - start))
            input("(Enter untuk melanjutkan)")
            return False
        else:
            print("Data yang anda masukkan bukan angka")
            input("(Enter untuk mengulangi)")

while True:
    os.system('clear')
    print("=============================")
    print("=       BINARY SEARCH       =")
    print("=                           =")
    print("=  1. Start Program        =")
    print("=  2. Exit                  =")
    print("=                           =")
    print("=          CREATOR          =")
    print("=  Achmad Musyaffa Taufiqi  =")
    print("    Teknik Informatika A    ")
    print("          04319023          ")
    print("=============================")
    pil = int(input("Masukkan pilihan: "))
    if pil == 1 :
        start()
    elif pil == 2:
        exit()
    else:
        print("Pilihan salah..")
        input("(Enter untuk melanjutkan)")