print("""
*************************
Kullanıcı Girişi Programı
*************************
""")

sys_kullanici_adı = "coqqomiq"
sys_şifre = "sanane123"

giriş_hakki = 3

while True:
    kullanıcı_adı=input("Kullanıcı Adınızı Giriniz:")
    şifre = input("Şifreyi giriniz:")

    if kullanıcı_adı != sys_kullanici_adı and şifre == sys_şifre:
        print("Kullanıcı Adınız Hatalı..")
        giriş_hakki -= 1

    elif kullanıcı_adı == sys_kullanici_adı and şifre != sys_şifre:
        print("Şifreniz Hatalı..")
        giriş_hakki -= 1

    elif kullanıcı_adı != sys_kullanici_adı and şifre != sys_şifre:
        print("Şifreniz Ve Kullanıcı Adınız Hatalı..")
        giriş_hakki -= 1

    else:
        print("Başarıyla Giriş Yapıldı...")
        break

    if giriş_hakki == 0:
        print("Giriş Hakkınız Bitmiştir.....")
        break
