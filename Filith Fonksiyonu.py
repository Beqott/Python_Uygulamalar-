def ücgen_mi(a,b,c):
    if a-b<c<a+b:
        return a,b,c
    elif a-c<b<a+c:
        return a,b,c
    elif b-c<a<b+c:
        return a,b,c
    else:
        print("Üçgen Oluşturmaz")
