import math

def No4():
    print("Masukkan jari jari lingkaran")
    x = int(input()) # jari jari lingkaran
    print("Masukkan Tinggi Lingkaran")
    Y = int(input()) # Tinggi kerucut

    Alas = 3.14 * x * x
    Selimut = (x * x) + (Y * Y)
    HasilS = math.sqrt(Selimut)  # hitung selimut
    Ls = 3.14*x*HasilS           # Hitung Luas selimut
    LpK = Alas + Ls              # Luas permukaan kerucut

    Volume = (3.14 * x * x * Y) / 3
    
    print("Luas permukaan kerucut adalah " + str(LpK) + " cm")
    print("Volume kerucut adalah " + str(Volume) + " cm")
No4()