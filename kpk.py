from collections import Counter

print("Perhitungan KPK Dan FPB\nPilih 1 untuk KPK dan 2 untuk FPB\n1.Perhitungan KPK\n2.Perhitungan FPB\nSilahkan Di pilih angka nya:")
try:
    jawaban_user = input()
    konversi_jawaban_user = int(jawaban_user)

    if konversi_jawaban_user == 1 :
        print("----Selamat Datang di Kalkulator KPK----\nSilahkan Masukkan dua angka:")
        print("Angka Pertama:")
        angka1 = int(input())
        print("Angka Kedua:")
        angka2 = int(input())
        if angka2 % angka1 == 0:
            print("hasil KPK nya", angka2)
        elif angka1 % angka2 == 0:
            print("Hasil KPK nya", angka1)
        else:
            def pencarian_bilangan_prima(angka1):
                factors_angka1 = []
                while angka1 % 2 == 0:
                    factors_angka1.append(2)
                    angka1 = angka1 // 2

                for i in range(3,int(angka1**0.5) + 1,2):
                    while angka1 % i == 0:
                        factors_angka1.append(i)
                        angka1 = angka1  // i

                if angka1 > 2:
                    factors_angka1.append(angka1)

                return factors_angka1
            
            def pencarian_prima_angka2(angka2):
                factors_angka2 = []
                while angka2 % 2 == 0:                    
                    factors_angka2.append(2)                   
                    angka2 = angka2 // 2

                for i in range(3,int(angka2**0.5) + 1,2):
                        while angka2 % i == 0:
                            factors_angka2.append(i)
                            angka2 = angka2  // i

                if angka2 > 2:
                        factors_angka2.append(angka2)
                    
                return factors_angka2
              
            hasil_prima_angka1 =  Counter(pencarian_bilangan_prima(angka1))
            hasil_prima_angka2 =  Counter(pencarian_bilangan_prima(angka2))
            
            hasil_gabungan_angka = hasil_prima_angka1 | hasil_prima_angka2
            hasil = list(hasil_gabungan_angka.elements())
            
            def perhitungan_kpk(hasil):
                nilai = 1
                for i in hasil:
                    nilai *= i
                return nilai

            print("Hasil nilai KPK nya Adalah", perhitungan_kpk(hasil))
            
    elif konversi_jawaban_user == 2 :
        print("----Selamat Datang di Kalkulator FOB----\nSilahkan Masukkan dua angka:")
        print("Angka Pertama:")
        angka1 = int(input())
        print("Angka Kedua:")
        angka2 = int(input())
        
        def pencarian_bilangan_prima(angka1):
            factors_angka1 = []
            while angka1 % 2 == 0:
                factors_angka1.append(2)
                angka1 = angka1 // 2

            for i in range(3,int(angka1**0.5) + 1,2):
                while angka1 % i == 0:
                    factors_angka1.append(i)
                    angka1 = angka1  // i

            if angka1 > 2:
                factors_angka1.append(angka1)

            return factors_angka1
            
        def pencarian_prima_angka2(angka2):
            factors_angka2 = []
            while angka2 % 2 == 0:                    
                    factors_angka2.append(2)                   
                    angka2 = angka2 // 2

            for i in range(3,int(angka2**0.5) + 1,2):
                        while angka2 % i == 0:
                            factors_angka2.append(i)
                            angka2 = angka2  // i

            if angka2 > 2:
                        factors_angka2.append(angka2)
                    
            return factors_angka2
              
        hasil_prima_angka1 =  Counter(pencarian_bilangan_prima(angka1))
        hasil_prima_angka2 =  Counter(pencarian_bilangan_prima(angka2))
            
        hasil_gabungan_angka = hasil_prima_angka1 & hasil_prima_angka2
        hasil = list(hasil_gabungan_angka.elements())
        def perhitungan_fpb(hasil):
            nilai = 1
            for i in hasil:
                nilai *= i
                
            return nilai

        print("Hasil nilai FPB nya Adalah", perhitungan_fpb(hasil))
    else :
        print("anda tidak memilih pilihan yang ada")
except:
    print("Anda tidak Memasukkan angka")



