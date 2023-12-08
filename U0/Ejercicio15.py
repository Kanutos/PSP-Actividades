# Ejercicio 15: Crea un fichero de texto con el nombre y contenido que tú desees. Por ejemplo, Ejercicio15.txt. 
# Realiza un programa en Python que lea el fichero <<Ejercicio15.txt>> y muestre su contenido por pantalla sin espacios. 
# Por ejemplo, si el fichero contiene el siguiente texto “Hola que haces”, deberá mostrar “Holaquehaces”.

# Abre el archivo en modo lectura
with open('Ejercicio15.txt', 'r') as file:
    # Lee el contenido del archivo
    content = file.read()
    # Reemplaza los espacios en blanco con nada
    frase= content.replace(' ', '')
    # Imprime el contenido sin espacios
    print(frase)
