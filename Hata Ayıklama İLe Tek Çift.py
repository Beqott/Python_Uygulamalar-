def cift(sayı):
    if sayı % 2 == 0:
        return sayı

    raise ValueError






liste = [2,3,4,6,123,15,22,16,41,31,52]


for i in liste:
    try:
        print(cift(i))

    except ValueError:
        print("Tek Sayı:",i)
