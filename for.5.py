n=int(input('dati nr: '))
suma=0
for nr in range(1,n):
    if (nr%3==0) and (nr%5==0):
        suma+=nr #suma numerelor de la 1 la n(exclusiv)
print(suma)
