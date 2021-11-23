"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c

Deltayı Hesaplama:  b ** 2 -  4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)

"""


print("2.dereceden kök bulma programı")


a = int(input("X^2'nin katsayısını giriniz:"))
b = int(input("X'in katsayısını giriniz:"))
c = int(input("sabit sayıyı giriniz:"))


delta = b ** 2 - 4 * a * c

birinci_kok  = (-b - delta ** 0.5) / (2*a)
ikinci_kok  = (-b + delta ** 0.5) / (2*a)

print("Girdiğiniz denklemin kökleri\n birinci kök {}\n ikinci kök {}'tür".format(birinci_kok,ikinci_kok))
