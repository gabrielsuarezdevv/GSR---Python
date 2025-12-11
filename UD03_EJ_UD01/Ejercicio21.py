contador = 0
hayNegativos = False

while contador < 100:
    numero = float(input("Introduce un número: "))
    if numero < 0:
        hayNegativos = True
    contador += 1
    
if hayNegativos:
    print("Has introducido al menos un número negativo.")
else:
    print("No has introducido ningún número negativo.")