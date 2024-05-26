import itertools

print("----Selamat Datang Di Kalkulator Pencarian Akar----\nAnda ingin mencari akar berapa?")
try:
    jawaban_mencari_akar = float(input())
    print("Masukkan angka yang ingin di cari berdasarkan akar", int((jawaban_mencari_akar)))
    jawaban_angka_diakar = float(input())
    start = 1.0
    step = 0.1
    z = 0
    nilai_list = []
    while z < jawaban_mencari_akar:
        nilai_list.append(0)
        z += 1

    daftar_variabel = {}
    for i in range(len(nilai_list)):
       nama_variabel = f"j{i+1}"
       daftar_variabel[nama_variabel] = nilai_list[i]

    for i in range(1):
        result = 1

        for j in itertools.count(1):
            for key in daftar_variabel:
                daftar_variabel[key] = j

            result = 1   
            for value in daftar_variabel.values():
                result *= value

            if result == jawaban_angka_diakar or result > jawaban_angka_diakar:
                break

        if result == jawaban_angka_diakar:
            single_value = next(iter(daftar_variabel.values()))
            print(f"akar {int(jawaban_mencari_akar)} dari {int(jawaban_angka_diakar)} adalah {single_value}")
            break
        elif result > jawaban_angka_diakar:
            print(f"akar {int(jawaban_mencari_akar)} dari {int(jawaban_angka_diakar)} tidak dapat di temukan\ncoba akar yang lain(2,3,4,dst)")
            print(daftar_variabel)
except:
    print("Anda tidak memasukkan angka!")