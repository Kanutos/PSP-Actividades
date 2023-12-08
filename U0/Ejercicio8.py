#Ejercicio 8: Implementa un programa Python con un método llamado sum(int [] tabla) que muestre por pantalla el resultado
# de sumar todos los elementos de la tabla pasada como parámetro.

def sum(tabla):
    resultado = 0
    for num in tabla:
        resultado += num
    print("La suma del array es", resultado)

tabla = [19, 5, 20, 9, 25]
sum(tabla)