def No3():
    print("Masukkan panjang")
    Panjang = input()
    print("Masukkan lebar")
    Lebar = input()
    print("Masukkan Tinggi")
    Tinggi = input()

    Volume = int(Panjang) * int(Lebar) * int(Tinggi)
    Lp = (int(Panjang)*int(Lebar) + int(Panjang)*int(Tinggi) + int(Tinggi)*int(Lebar)) * 2

    print("Hasil Volume balok adalah " + str(Volume) + " cm")
    print("Hasil Luas permukaan Balok adalah " + str(Lp) + " cm")

No3()