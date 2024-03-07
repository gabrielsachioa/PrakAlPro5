jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))

def program_ips(jumlah_matkul):
    jumlah_sks = 3
    total_poin = 0

    for i in range(jumlah_matkul):
        huruf_nilai = input(f"Nilai MK {i + 1}: ")

        if huruf_nilai == "A":
            poin = 4
        elif huruf_nilai == "B":
            poin = 3
        elif huruf_nilai == "C":
            poin = 2
        elif huruf_nilai == "D":
            poin = 1
        else:
            poin = 0

        total_poin += poin

    hasil_ips = (jumlah_sks * total_poin)/ (jumlah_sks * jumlah_matkul)
    return ('%.2f' % hasil_ips)


nilai_ips = program_ips(jumlah_matkul)
print(f"Nilai IPS Anda semester ini {nilai_ips}")

