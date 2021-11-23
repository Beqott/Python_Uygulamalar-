print("""
Mükemmel Sayı bulma programı

""")


sayı = int(input("Sayıyı Giriniz:"))

i = 1
toplam = 0

while (i < sayı):
    if sayı % i == 0:
        toplam += i

    i += 1


if toplam == sayı:
    print("Mükemmel Sayıdır",sayı)


else:
    print("Mükemmel Sayı Değildir")
