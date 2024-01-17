"""
Your module description
"""
print("Ingresa un número no negativo para calcular el factorial:")
numero = int(input())

while numero < 0:
    print("Error, por favor ingresa un número válido:")
    numero = int(input())



factorial = 1


for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es: {factorial}")
