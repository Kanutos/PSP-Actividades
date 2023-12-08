# Ejercicio 10:  Implementa un método Python llamado mayorYmenor, el cual recibe como parámetro una tabla de Strings
# y muestra por pantalla el String con mayor longitud y el String con menor longitud.

def mayorYmenor(strings):
    # Encuentra el string con mayor longitud
    mayor = max(strings, key=len)
    # Encuentra el string con menor longitud
    menor = min(strings, key=len)

    # Imprime los resultados
    print("El string con mayor longitud es: ", mayor)
    print("El string con menor longitud es: ", menor)

# Prueba la función con una lista de strings
mayorYmenor(["Esternocleidomastoideo", "Mamarracho", "juerga", "Programación"])
