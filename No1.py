def Myfunc():
    x = 4
    y = 5
    print("Masukkan Suhu Celcius")
    Suhu = input()
    Ream = (int(Suhu) * 4)/5
    print("Hasil dari celcius ke reamur adalah " + str(Ream) + " derajat") #Celcius to reamur

    
    Fahren = (int(Suhu)*9)/5 + 32
    print('Hasil dari celcius ke fahreinheit ' + str(Fahren) + " derajat") # Celcius to Fahreinheit

    Celci = (Ream*5)/4
    print("Hasil dari Reamur ke Celcius " + str(Celci) + " derajati") # Reamur to Celcius
    
    Fahreinheit = (Ream*2.25) + 32
    print("Hasil dari Reamur ke Fahreinheit " + str(Fahreinheit) + " derajat") # Reamur to Fahreinheit
    
    remur = (Fahreinheit - 32) * 4 / 9
    print("Hasil dari Fahreinheit ke reamur adalah " + str(remur) + " derajat") # Fahreinheit to reamur
    
    Cel = (Fahren - 32) * 5 / 9
    print("Hasu dari Fahreinheit ke celcius adalah " + str(Cel) + " derajat") # Fahreinheit to celcius
    

    
Myfunc()
