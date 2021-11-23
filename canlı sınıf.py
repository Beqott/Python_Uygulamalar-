class canlı():
    def __init__(self,adı,habitat,beslenme,türü,ayak_sayısı):
        self.adı = adı
        self.habitat=habitat
        self.beslenme=beslenme
        self.türü=türü
        self.ayak_sayısı=ayak_sayısı







insan=canlı("İnsan","Doğa","Hem Etçil Hem Otçul","Hayvan",2)

a = input("İsim Gir:")

if a == "insan":
    print("ADI:",insan.adı)
    print("Yaşam alanı:",insan.habitat)
    print("Beslenme:",insan.beslenme)
    print("Türü:",insan.türü)
    print("Ayak Sayısı:",insan.ayak_sayısı)
