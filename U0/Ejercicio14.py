# Ejercicio 14: Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
#             - 1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.
#             - 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
#             - 3. Salir del Programa.

def volcar_numeros_pares():
    with open("numeros_pares.txt", "w") as archivo:
        for numero in range(0, 101, 2):
            archivo.write(f"{numero}\n")
    print("Números pares del 0 al 100 volcados en el archivo 'numeros_pares.txt'.")

def mostrar_contenido():
    try:
        with open("numeros_pares.txt", "r") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo 'numeros_pares.txt':")
            print(contenido)
    except FileNotFoundError:
        print("El archivo 'numeros_pares.txt' no existe o está vacío.")

while True:
    print("\nMenú:")
    print("1. Volcar números pares entre 0 y 100 en un archivo.")
    print("2. Mostrar contenido del archivo.")
    print("3. Salir del programa.")
    opcion = input("Elige una opción (1/2/3): ")

    if opcion == "1":
        volcar_numeros_pares()
    elif opcion == "2":
        mostrar_contenido()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
