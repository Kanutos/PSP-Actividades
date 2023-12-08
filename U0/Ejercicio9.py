# Ejercicio 9:  Implementa un programa Python con un método llamado indexContains(String[] tabla, String cadena) 
# que devuelva el índice de la tabla cuyo valor es igual al valor de “cadena”.
# En caso de no haber ningún valor igual, devuelve -1


def indexContains(tabla, cadena):
    try:
        # Intenta encontrar el índice de la cadena en la tabla
        index = tabla.index(cadena)
    except ValueError:
        # Si la cadena no se encuentra en la tabla, devuelve -1
        index = -1
    return index

# Prueba la función con una lista de strings y una cadena
print(indexContains(["Hola", "Mundo", "Python", "Programación"], "Python"))