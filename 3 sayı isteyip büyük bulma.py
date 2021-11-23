




a = int(input("Birinci Sayıyı Giriniz:"))
b = int(input("İkinci Sayıyı Giriniz:"))
c = int(input("Üçüncü Sayıyı Giriniz:"))

if a > b and a > c:
    print("Girdiğiniz En büyük sayı {}'dır".format(a))

elif b > a and b > c:
    print("Girdiğiniz En büyük sayı {}'dır".format(b))

elif c > a and c > b:
    print("Girdiğiniz En büyük sayı {}'dır".format(c))


else:
    print("Girdiğiniz Sayılar Eşittir ve {}'dur".format(a))
