def ekstra(fonk):
    def wrapper():
        
        for sayı in range(2,1001):
            i = 1
            toplam = 0
        
            while (i < sayı):
                if sayı %i ==0:
                    toplam += i

                i += 1

            if toplam == sayı:
                print("Mükemmel Sayıdır",sayı)
    fonk()
    return wrapper









@ekstra
def asal_sayılar():
    print("Asal Sayılar....")

    for sayı in range(2,1001):
        i = 2
        say = 0
        while (i < sayı):
            if sayı %i == 0:
                say +=1

            i +=1

        if (say==0):
            print(sayı)

asal_sayılar()
