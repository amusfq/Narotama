import time

A = [64, 25, 12, 22, 11]
print("SELECTION SORT")
print()
print("Array Awal : %s" % A)
start = time.time()
for i in range(len(A)):
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    temp = A[i]
    A[i] = A[min_idx]
    A[min_idx] = temp
    print("#%i - %s" % (i, A))

end = time.time()
print("Array akhir : %s" %A)
print()
print("Selesai dalam %f detik" % (end - start))
