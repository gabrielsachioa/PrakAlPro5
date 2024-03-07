# CARA 1
def ganjil(batas_bawah, batas_atas):

    langkah = 1 if batas_bawah < batas_atas else -1

    for i in range(batas_bawah, batas_atas, langkah):
        if i % 2 == 1:
            print(i)

ganjil(10, 30)
print("======================")
ganjil(97, 82)