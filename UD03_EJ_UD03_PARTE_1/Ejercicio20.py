nota = float(input("Introduce una calificación numérica entre 0 y 10: "))
if 0 <= nota < 3:
    print("La calificación alfabética es: Muy Deficiente")
elif 3 <= nota < 5:
    print("La calificación alfabética es: Insuficiente")
elif 5 <= nota < 6:
    print("La calificación alfabética es: Suficiente")
elif 6 <= nota < 7:
    print("La calificación alfabética es: Bien")
elif 7 <= nota < 9:
    print("La calificación alfabética es: Notable")
elif 9 <= nota <= 10:
    print("La calificación alfabética es: Sobresaliente")
else:
    print("La calificación introducida no es válida")
