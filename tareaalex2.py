"""
Your module description
"""
print("Ingresa un número para saber la cantidad de pares e impares:")
numero = int(input())


pares = 0
impares = 0


for i in range(1, numero + 1):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"En el rango del 1 al {numero} hay {pares} números pares y {impares} números impares.")
