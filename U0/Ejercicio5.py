# Ejercicio 5:  Implementa un programa Python que solicite al usuario una cadena de caracteres (String) y muestre por pantalla
# el número de veces que aparece la sub-cadena “aaa” dentro de dicho String.

# Solicitar al usuario una cadena de caracteres
cadena_usuario = input("Por favor, introduce una cadena de caracteres: ")

# Contar el número de veces que aparece "aaa"
numero_de_veces = cadena_usuario.count("aaa")

# Imprimir el resultado
print("La subcadena 'aaa' aparece {} veces en la cadena introducida.".format(numero_de_veces))