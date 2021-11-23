print(""" BASİT HESAP MAKİNESİ PROGRAMINA HOŞGELDİNİZ


EĞER TOPLAMA YAPMAK İSTİYORSANIZ "1" TUŞUNA BASINIZ
EĞER ÇIKARMA YAPMAK İSTİYORSANIZ "2" TUŞUNA BASINIZ
EĞER ÇARPMA YAPMAK İSTİYORSANIZ "3" TUŞUNA BASINIZ
EĞER BÖLME YAPMAK İSTİYORSANIZ "4" TUŞUNA BASINIZ

""")

işlem = int(input("Lütfen Yapmak istediğiniz işlem numarasını giriniz."))


if işlem == 1:
    a = float(input("Birinci Sayıyı giriniz:"))
    b = float(input("İkinci Sayıyı giriniz:"))
    print("Girdiğiniz Sayıların toplamı {}'dır".format(a+b))


elif işlem == 2:
    a = float(input("Birinci Sayıyı giriniz:"))
    b = float(input("İkinci Sayıyı giriniz:"))
    print("Girdiğiniz Sayıların Farkı {}'dır".format(a-b))


elif işlem == 3:
    a = float(input("Birinci Sayıyı giriniz:"))
    b = float(input("İkinci Sayıyı giriniz:"))
    print("Girdiğiniz Sayıların Çarpımı {}'dır".format(a*b))


elif işlem == 4:
    a = float(input("Birinci Sayıyı giriniz:"))
    b = float(input("İkinci Sayıyı giriniz:"))
    print("Girdiğiniz Sayıların bölümü {}'dir".format(a/b))


else:
    print("Lütfen Geçerli bi işlem numarası giriniz")


