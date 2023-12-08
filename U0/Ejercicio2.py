# Ejercicio 2:  Escribe un programa Python que pregunte al usuario por 10 números enteros y 
# muestre por pantalla el número total de veces que el usuario ha introducido el 0, el número 
# total de enteros mayores que 0 introducidos y el número total de enteros menores que 0 introducidos.

# Paso 1: Crear una lista vacía
numeros = []

# Paso 2: Pedir al usuario que introduzca 10 números enteros
for i in range(10):
    num = int(input("Introduce un número entero: "))
    numeros.append(num)

# Paso 3: Contar el número de veces que el usuario ha introducido 0, números mayores que 0 y números menores que 0
cero = numeros.count(0)
mayores_cero = sum(1 for i in numeros if i > 0)
menores_cero = sum(1 for i in numeros if i < 0)

print("El número total de veces que el usuario ha introducido el 0 es: ", cero)
print("El número total de enteros mayores que 0 introducidos es: ", mayores_cero)
print("El número total de enteros menores que 0 introducidos es: ", menores_cero)