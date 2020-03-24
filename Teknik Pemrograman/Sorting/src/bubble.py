import time
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
      for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
          temp = arr[j]
          arr[j] = arr[j + 1]
          arr[j + 1] = temp
        print("#%i-%i - %s" % (i, j, arr))

A = [64, 25, 12, 22, 11]
print("BUBBLE SORT")
print()
print("Array awal : %s" % A)
start = time.time()
bubbleSort(A)
end = time.time()
print("Array Akhir : %s" %A)
print()
print("Selesai dalam %f detik" % (end - start))
