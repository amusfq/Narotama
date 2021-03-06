import time
import os

def selection():
    while True:
        os.system('clear')
        print("=============================")
        print("        Selection Sort       ")
        print("=============================")
        print("Masukkan array angka")
        print('(pisahkan dengan koma)')
        inp = input()
        if inp.replace(',', '').isnumeric():
            A = inp.split(',')
            print("Array Awal : %s" % A)
            start = time.time()
            for i in range(len(A)):
                min_idx = i
                for j in range(i + 1, len(A)):
                    if int(A[min_idx]) > int(A[j]):
                        min_idx = j

                temp = A[i]
                A[i] = A[min_idx]
                A[min_idx] = temp
                print("#%i - %s" % (i, A))

            end = time.time()
            print("Array akhir : %s" % A)
            print()
            print("Selesai dalam %f detik" % (end - start))
            input("(Enter untuk melanjutkan)")
            return False
        else:
            print("Data yang anda masukkan bukan angka")
            input("(Enter untuk melanjutkan)")


def bubble():
    while True:
        os.system('clear')
        def bubbleSort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if int(arr[j]) > int(arr[j + 1]):
                        temp = arr[j]
                        arr[j] = arr[j + 1]
                        arr[j + 1] = temp
                    print("#%i-%i - %s" % (i, j, arr))

        print("=============================")
        print("        Bubble Sort       ")
        print("=============================")
        print("Masukkan array angka")
        print('(pisahkan dengan koma)')
        inp = input()
        if inp.replace(',', '').isnumeric():
            A = inp.split(',')
            print("BUBBLE SORT")
            print()
            print("Array awal : %s" % A)
            start = time.time()
            bubbleSort(A)
            end = time.time()
            print("Array Akhir : %s" % A)
            print()
            print("Selesai dalam %f detik" % (end - start))
            input("(Enter untuk melanjutkan)")
            return False
        else:
            print("Data yang anda masukkan bukan angka")
            input("(Enter untuk melanjutkan)")

while True:
    os.system('clear')
    print("=============================")
    print("=  PILIH ALGORITMA SORTING  =")
    print("=                           =")
    print("=  1. Selection Sort        =")
    print("=  2. Bubble Sort           =")
    print("=  3. Exit                  =")
    print("=                           =")
    print("=============================")
    pil = int(input("Masukkan pilihan: "))
    if pil == 1 :
        selection()
    elif pil == 2:
        bubble()
    elif pil == 3:
        exit()
    else:
        os.system('clear')
        print("Pilihan salah..")
        input("(Enter untuk melanjutkan)")