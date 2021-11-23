print("""
BİR DİK ÜÇGENİN HİPOTENÜS UZUNLUĞUNU BULMA PROGRAMI
""")

a = int(input("Üçgenin Bir kenarını giriniz:"))
b = int(input("Üçgenin Diğer kenarını giriniz:"))


hipotenus = (a**2 + b**2) ** 0.5


print("Dik üçgeninizin Hipotenüs uzunluğu {}'dur".format(hipotenus))
