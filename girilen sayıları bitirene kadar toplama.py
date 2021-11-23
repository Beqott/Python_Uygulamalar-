print("""
*******************************************
'q' TUŞUNA BASANA KADAR YAZDIĞINIZ SAYILARI TOPLAYAN PROGRAM
*******************************************
""")



toplam = 0

while True:
    sayı = input("Sayı:")

    if sayı == "q":
        print("Girdiğiniz Sayıların Toplamı: {}".format(toplam))
        break
    else:
        sayı = int(sayı)


    toplam += sayı
