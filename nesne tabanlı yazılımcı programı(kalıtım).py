class çalışan():
    def __init__(self,isim,soyisim,maaş,departman):
        self.isim=isim
        self.soyisim=soyisim
        self.maaş=maaş
        self.departman=departman


    def bilgilerigöster(self):
        print("""
        Çalışan Bilgileri;
        İsim = {}
        Soyisim = {}
        Maaş = {}
        Departman = {}
        """.format(self.isim,self.soyisim,self.maaş,self.departman))


    def departman_degiştir(self,yeni_departman):

        self.departman = yeni_departman




class yönetici(çalışan):
    def __init__(self,isim,soyisim,maaş,departman,sorumluluk):
        super().__init__(isim,soyisim,maaş,departman)

        self.sorumluluk = sorumluluk




    def bilgilerigöster(self):
        print("""
        Çalışan Bilgileri;
        İsim = {}
        Soyisim = {}
        Maaş = {}
        Departman = {}
        Sorumlu Olduğu Kişi Sayısı = {}
        """.format(self.isim,self.soyisim,self.maaş,self.departman,self.sorumluluk))



berkay = yönetici("Berkay","Uluğ",3000,"Bilişim",21)

berkay.bilgilerigöster()
