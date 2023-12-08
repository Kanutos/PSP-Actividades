# Ejercicio 12: Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crea sus métodos get, set y toString. Tendrá dos métodos especiales:
#                  - ingresar(double cantidad): se ingresa una cantidad a la cuenta si la cantidad introducida es negativa, no se hará nada.
#                  - retirar(double cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0.
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.cantidad:
                self.cantidad -= cantidad
            else:
                self.cantidad = 0

    def get(self):
        return self.cantidad

    def set(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.cantidad:.2f}€"

# Ejemplo de uso de la clase Cuenta
mi_cuenta = Cuenta("Juan Pérez", 1000.50)
print(mi_cuenta)  # Titular: Juan Pérez, Saldo: 1000.50€

mi_cuenta.ingresar(500)
print(mi_cuenta)  # Titular: Juan Pérez, Saldo: 1500.50€

mi_cuenta.retirar(2000)
print(mi_cuenta)  # Titular: Juan Pérez, Saldo: 0.00€

mi_cuenta.set(1500)
print(mi_cuenta)  # Titular: Juan Pérez, Saldo: 1500.00€
