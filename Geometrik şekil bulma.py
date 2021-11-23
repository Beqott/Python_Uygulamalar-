print("""
GEOMETRİK ŞEKİL HESAPLAMA PROGRAMI

DÖRTGENİN TİPİNİ BULMAK İÇİN 1 
ÜÇGENİN TİPİNİ BULMAK İÇİN 2 TUŞUNA BASINIZ

"""

)

işlem = int(input("İşlem Numarasını giriniz:"))

if işlem == 1 :
    a = int(input("dörtgenin bir kenar uzunluğunu giriniz:"))
    b = int(input("dörtgenin karşısındaki kenar uzunluğunu giriniz:"))
    c = int(input("dörtgenin diğer kenar uzunluğunu giriniz:"))
    d = int(input("dörtgenin karşısındaki kenar uzunluğunu giriniz:"))

    if a == b == c == d:
        print("Dörtgen Tipiniz Kare'dir")


    elif a == b or c == d:
        print("Dörtgen Tipiniz Dikdörtgendir")

    else:
        print("Dörtgen Tipiniz Sıradan Dörtgendir")


elif işlem == 2:
    a = int(input("Üçgenin birinci kenar uzunluğunu giriniz:"))
    b = int(input("Üçgenin ikinci kenar uzunluğunu giriniz:"))
    c = int(input("Üçgenin üçüncü kenar uzunluğunu giriniz::"))

    if abs(a-b) < c < abs(a+b) or abs(a-c) < b < abs(a+c) or abs(b-c) < a < abs(c+b):
        print("Belirttiğiniz uzunluklar üçgen oluşturur,Lütfen Bekleyiniz..")
        print("Sıradan Üçgendir")


        if a == b == c:
            print("Belirttiğiniz üçgen Eşkenar Üçgendir")

        elif a == b or b == c or c == a:
            print("Belirttiğiniz üçgen ikizkenar üçgendir")

    else:
        print("belirttiğiniz uzunluklar üçgen belirtmez.")


else:
    print("GEÇERSİZ ŞEKİL")


    
    
