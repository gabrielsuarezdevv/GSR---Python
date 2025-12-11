import math

radio = float(input("Introduce la longitud del radio: "))
diametro = radio * 2
longitud_circunferencia = math.pi * diametro
area_circulo = math.pi * (radio ** 2)
volumen_esfera = (4/3) * math.pi * (radio ** 3)
print("La longitud de la circunferencia es:", longitud_circunferencia)
print("El área del círculo es:", area_circulo)
print("El volumen de la esfera es:", volumen_esfera)