bil1 = input("Masukkan bilangan #1 : ")
bil2 = input("Masukkan bilangan #2 : ")

print("Bilangan sebelum di swap")
print("Bilangan #1 :", bil1)
print("Bilangan #2 :", bil2)

def tukar(first, second):
   return(second, first)

bil1, bil2 = tukar(bil1, bil2)

print()
print("Bilangan setelah di swap")
print("Bilangan #1 :", bil1)
print("Bilangan #2 :", bil2)
