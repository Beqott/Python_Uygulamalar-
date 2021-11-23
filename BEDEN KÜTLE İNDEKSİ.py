print("""
Beden Kitle İndeksi hesaplama programı
""")


boy = float(input("Lütfen Boyunuzu Giriniz(metre cinsinden):"))
kilo = int(input("Lütfen Kilonuzu Giriniz:"))


BKI = kilo / (boy ** boy)

print("Beden Kitle İndeksiniz {}'dir".format(BKI))
