def ekstra(fonk):

    def wrapper(sayılar):
        çiftler_toplamı =0
        çiftler_sayısı = 0
        tekler_toplamı=0
        tekler_sayısı=0

        for sayı in sayılar:
            if (sayı % 2 == 0):
                çiftler_toplamı += sayı
                çiftler_sayısı += 1

            else:
                tekler_toplamı += sayı
                tekler_sayısı +=1
                
        print("Teklerin Ortalaması",tekler_toplamı/tekler_sayısı)
        print("Çiftlerin Ortalaması",çiftler_toplamı/çiftler_sayısı)

        fonk(sayılar)
    return wrapper


@ekstra
def ortalamabul(sayılar):

    toplam = 0

    for sayı in sayılar:
        toplam +=sayı

    print("Genel Ortalama:",toplam/len(sayılar))

ortalamabul([12,21,32,11,23,54,51,24,456,687,67,43])
