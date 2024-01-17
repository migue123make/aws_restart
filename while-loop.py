"""
Your module description
"""
import random # biblioteca para utilizar numeros aleatorios
print("\t\tBienvenidos a nuestro juego de adivina el numero")
print("\nLa regla es facil, pensare un numero y tu lo adivinas")

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    #continuo con el juego
    guess = int(input("Adivina un numero entre 1 y 10"))
    #si el numero que ingreso al que tengo 
    if guess == number:
        print(f"!felicidades el numero es {guess}")
        isGuessRight = True
    else:
        print("Intenta de nuevo")