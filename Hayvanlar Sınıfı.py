class hayvanlar():
    def __init__(self,adı,ayak_sayısı,beslenme_şekli,yaşam_alanı,özellikleri):
        self.adı=adı
        self.ayak_sayısı=ayak_sayısı
        self.beslenme_şekli=beslenme_şekli
        self.yaşam_alanı=yaşam_alanı
        self.özellikleri=özellikleri


    def bilgilerigöster(self):
        print("""
        Hayvanın Özeliikleri:
        İsmi = {}
        Ayak Sayısı= {}
        Beslenme Şekli = {}
        Yaşam Alanı = {}
        Özellikleri = {}

        """.format(self.adı,self.ayak_sayısı,self.beslenme_şekli,self.yaşam_alanı,self.özellikleri))




class köpek(hayvanlar):
    def __init__(self,adı,ayak_sayısı,beslenme_şekli,yaşam_alanı,özellikleri,avcılık):
        super().__init__(adı,ayak_sayısı,beslenme_şekli,yaşam_alanı,özellikleri)

        self.avcılık = avcılık


    def bilgilerigöster(self):
        print("""
        Hayvanın Özeliikleri:
        İsmi = {}
        Ayak Sayısı= {}
        Beslenme Şekli = {}
        Yaşam Alanı = {}
        Özellikleri = {}
        Avcılık Düzeyi = {}

        """.format(self.adı,self.ayak_sayısı,self.beslenme_şekli,self.yaşam_alanı,self.özellikleri,self.avcılık))

class Atlar(hayvanlar):
    def __init__(self, adı, ayak_sayısı, beslenme_şekli, yaşam_alanı, özellikleri,tarihi_önemi):
        super().__init__(adı, ayak_sayısı, beslenme_şekli, yaşam_alanı, özellikleri)

        self.tarihi_önemi=tarihi_önemi

    def bilgilerigöster(self):
        print("""
        Hayvanın Özeliikleri:
        İsmi = {}
        Ayak Sayısı= {}
        Beslenme Şekli = {}
        Yaşam Alanı = {}
        Özellikleri = {}
        Tarihi Önemi = {}
            
        """.format(self.adı, self.ayak_sayısı, self.beslenme_şekli, self.yaşam_alanı, self.özellikleri,
                     self.tarihi_önemi))



class Kuşlar(hayvanlar):
    def __init__(self, adı, ayak_sayısı, beslenme_şekli, yaşam_alanı, özellikleri, dogurma_sekli):
        super().__init__(adı, ayak_sayısı, beslenme_şekli, yaşam_alanı, özellikleri)

        self.dogurma_sekli=dogurma_sekli

    def bilgilerigöster(self):
        print("""
           Hayvanın Özeliikleri:
           İsmi = {}
           Ayak Sayısı= {}
           Beslenme Şekli = {}
           Yaşam Alanı = {}
           Özellikleri = {}
           Doğurma Şekli = {}

           """.format(self.adı, self.ayak_sayısı, self.beslenme_şekli, self.yaşam_alanı, self.özellikleri,
                      self.dogurma_sekli))





köpekler = köpek("Köpek",4,"Etçil","Kırsal ALan",["İnsanlara Son Derece Sadıktırlar","Korumacıdırlar","Hızlı Koşarlar"],"Son Derece İyi Avcıdırlar")




Atlar = Atlar("At",4,"Otçul","Kırsal Alan",["Hızlıdırlar","Binek Hayvan","Memelidir"],"İnsanlık Tarihi Boyunca Hem Binek Hem Savaş olsun bir çok alanda çok yardımcı olan hayvanlardır")




Kuşlar = Kuşlar("Kuş",2,"Hem Etçil Hem Otçul(türüne göre)","Ormanlık Alan","Uçabilen Hayvanlardır,Bazı Türleri Uçamaz,Memeli Olanıda Vardır,Avcıdırlar genelde","Yumurtlayarak Doğururlar(Yarasa Hariç)")


print("""
Köpek = 1
At = 2
Kuş = 3
""")


while True:
    işlem = input("İşleminizi Giriniz:")

    if işlem == "1":
        köpekler.bilgilerigöster()


    elif işlem =="2":
        Atlar.bilgilerigöster()


    elif işlem == "3":
        Kuşlar.bilgilerigöster()


    else:
        print("Daşşak mı Geçiyon Siktir Git")
        break
        
        
    










