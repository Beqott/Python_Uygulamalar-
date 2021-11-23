print("""
*****************************************
Faktoriyel bulma programı

Çıkmak için 'q'ya basınız

*****************************************

""")

while True:
    işlem = input("Sayıyı Giriniz:")

    if işlem == "q":
        break

    else:
        işlem = int(işlem)


        faktoriyel = 1
    for i in range(2,işlem+1):
        faktoriyel *= i
        print("faktoriyel",faktoriyel)
