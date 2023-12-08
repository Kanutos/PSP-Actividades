# Ejercicio 3:  ¡IMPLEMENTA TU PRIMER JUEGO! Realiza un programa Python que adivine el número. 
# El programa generará un número aleatorio entre 0 y 20 y luego irá pidiendo números al usuario 
# indicando “mayor” o “menor” según sea mayor o menor con respecto al número generado aleatoriamente.
# El proceso termina cuando el usuario acierta, y deberá mostrar un mensaje de felicitaciones junto al número de intentos que ha necesitado el usuario.
6
import random

# Genera un número aleatorio entre 0 y 20
numero_aleatorio = random.randint(0, 20)

# Inicializa el contador de intentos
intentos = 0

while True:
    # Pide al usuario que adivine el número
    numero_usuario = int(input("Adivina el número entre 0 y 20: "))
    intentos += 1

    # Comprueba si el número del usuario es mayor, menor o igual al número aleatorio
    if numero_usuario > numero_aleatorio:
        print("Menor")
    elif numero_usuario < numero_aleatorio:
        print("Mayor")
    else:
        print(f"Felicitaciones! Has adivinado el número después de {intentos} intentos.")
        break