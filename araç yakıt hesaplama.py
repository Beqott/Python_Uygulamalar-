print("""
Aracın yaktığı yakıt fiyatını hesaplama
""")


a = float(input("Araç Kilometrede Ne kadar yakıyor:"))
b = int(input("Araç kaç kilometre yol yaptı:"))


tutar = a*b

print("Ödemeniz gereken tutar {}'TLdir".format(tutar))
