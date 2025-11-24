tamaño_figura = 5
altura = 2 * tamaño_figura - 1

print(" " * (tamaño_figura - 1), end="")
print("*")

for i in range(2, tamaño_figura):
    print(" " * (tamaño_figura - i), end="")
    print("*", end="")
    print(" " * (i * 2 - 3), end="")
    print("*")
    
for i in range(tamaño_figura, 2, -1):
    print(" " * (tamaño_figura - i), end="")
    print("*", end="")
    print(" " * (i * 2 - 3), end="")
    print("*")
    
print(" " * (tamaño_figura - 1), end="")
print("*")

    