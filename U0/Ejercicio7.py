# Ejercicio 7:  Implementa un programa Python que solicite al usuario una cadena de caracteres y devuelva dicha cadena, pero al revés.

cadena = input("Ingrese una cadena de caracteres: ")
cadena_al_reves = ''.join(reversed(cadena))
print("La cadena al revés es:", cadena_al_reves)