import math as matematik

print("""
GELİŞMİŞ HESAP MAKİNESİ
*******************************************************************************************
1)Faktoriyel Bulmak İçin '1' e basınız


2) Girdiğiniz 2 sayının EBOB'unu bulmak için '2'ye basınız


3)Yazdığınız Birinci Değerin İkincisine Göre Logaritmasını almak için 3'e basınız


4)Girdiğiniz Sayının Karekökünü hesaplamak için 4'e basınız


Çıkmak için 'q'ya basınız.

*******************************************************************************************
""")



while True:
    sayı = input("Lütfen Seçmek İstediğiniz İşlemi Giriniz:")

    if sayı == "q":
        print("Programdan Çıkış Yapılıyor")
        break

    else:
        sayı = int(sayı)



    if sayı == 1:
        fak = int(input("Sayıyı Giriniz:"))
        print(matematik.factorial(fak))

    elif sayı == 2:
        a1=int(input("İlk Sayıyı Giriniz:"))
        a2=int(input("İkinci Sayıyı Giriniz:"))
        print(matematik.gcd(a1,a2))

    elif sayı == 3:
        b1=int(input("İlk Sayıyı Giriniz:"))
        b2=int(input("İkinci Sayıyı Giriniz:"))
        print(matematik.log(b1,b2))

    elif sayı == 4:
        sq = int(input("Sayıyı Giriniz:"))
        print(matematik.sqrt(sq))

    else:
        print("Geçersiz İşlem Numarası")
        
