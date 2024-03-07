# CARA 1
batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))

def ganjil(batas_bawah, batas_atas):

    langkah = 1 if batas_bawah < batas_atas else -1

    for i in range(batas_bawah, batas_atas, langkah):
        if i % 2 == 1:
            print(i)

ganjil(batas_bawah, batas_atas)
