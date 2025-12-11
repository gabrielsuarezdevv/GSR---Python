num = int(input("Introduce un número entre 0 y 99999: "))
if 0 <= num <= 9:
    print("El número tiene 1 cifra")
elif 10 <= num <= 99:
    print("El número tiene 2 cifras")
elif 100 <= num <= 999:
    print("El número tiene 3 cifras")
elif 1000 <= num <= 9999:
    print("El número tiene 4 cifras")
elif 10000 <= num <= 99999:
    print("El número tiene 5 cifras")
else:
    print("El número no está entre 0 y 99999")