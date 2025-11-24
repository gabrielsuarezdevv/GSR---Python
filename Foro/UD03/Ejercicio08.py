tamaño_figura = 4
altura = 2 * tamaño_figura - 1

for i in range(1, tamaño_figura):
    print(" " * (tamaño_figura - i), end="")
    asteriscos = 2 * i - 1
    print("*" * (asteriscos), end="")
    print(" " * (tamaño_figura - i))

print("*" * altura)

for i in range(tamaño_figura - 1, 0, -1):
    print(" " * (tamaño_figura - i), end="")
    asteriscos = 2 * i - 1
    print("*" * (asteriscos), end="")
    print(" " * (tamaño_figura - i))
