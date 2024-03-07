bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan pertama: "))

def perkalian(bil1, bil2):
   
   hasil = 0

   for _ in range(bil1):
      hasil += bil2
   print(hasil)

perkalian(bil1, bil2)
