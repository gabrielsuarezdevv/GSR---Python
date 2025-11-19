altura = int(input("Introduce la altura de la figura: "))

print("4")

for i in range(1, altura - 1):
    
    print("4", end="")
    espacios = 2 * i - 1
    print(" " * espacios, end="") 
    print("4")

for _ in range(altura):
    
    print("4", end=" ") 