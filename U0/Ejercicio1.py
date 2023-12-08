1# Ejercicio 1: Implementa un programa Python que PREGUNTE al usuario por dos números enteros (x, y) y muestre por pantalla la suma, resta, multiplicación, división y resto de ambos, con el siguiente formato:
#                       x + y = …
#                       x – y = …
#                       x * y = …
#                       x / y = …
#                       x % y = …

x = int(input("Ingrese el primer número entero: "))
y = int(input("Ingrese el segundo número entero: "))

suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y
modulo = x % y

print(f"{x} + {y} = {suma}")
print(f"{x} - {y} = {resta}")
print(f"{x} * {y} = {multiplicacion}")
print(f"{x} / {y} = {division}")
print(f"{x} % {y} = {modulo}")