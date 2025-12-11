contador = 0
contadorPositivos = 0
contadorNegativos = 0

while contador < 100:
    numero = float(input("Introduce un número: "))
    if numero > 0:
        contadorPositivos += 1
    elif numero < 0:
        contadorNegativos += 1
    
    contador += 1

print("Has introducido", contadorPositivos, "números positivos y", contadorNegativos, "números negativos.")
    
    