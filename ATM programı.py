print("""
***********************************
ATM MAKİNESİ PROGRAMINA HOŞGELDİNİZ


ÇIKMAK İÇİN LÜTFEN 'q' ya basınız


1)Bakiye Sorgulamak için '1'i
2)Para Yatırmak için '2'yi
3)Para Çekmek için ise '3'ü Tuşlayınız
**************************************""")

bakiye = 1000

while True:
    işlem = int(input("Lütfen Yapmak İstediğiniz işlem numarasını tuşlayınız.."))

    if (işlem == "q"):
        print("Yine Bekleriz....")
        break

    if işlem == 1:
        print("Bakiyeniz {}'tldir".format(bakiye))
        

    elif işlem == 2:
        miktar = int(input("Yatırmak İstediğiniz Para Miktarını Giriniz:"))
        bakiye += miktar
        print("Yeni Bakiyeniz {}TL'dir".format(bakiye))
                     

    elif işlem == 3:

        miktar = int(input("Çekmek İstediğiniz Para Miktarını Giriniz:"))
        if bakiye - miktar < 0:
            print("Yetersiz Bakiye")
            continue
        bakiye -= miktar
        print("Bakiyeniz {}'tldir".format(bakiye))
            



    else:
        print("Geçersiz Tuşlama Yaptınız.....")
