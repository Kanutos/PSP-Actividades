"""Exercise 3: List all process in operative system with PID, and allow termination of one by PID"""

import psutil

def listado_de_procesos():
    print("Listado de procesos:")
    for process in psutil.process_iter(['pid', 'name']):
        print(f"PID: {process.info['pid']}, name: {process.info['name']}")

def finalizar_proceso(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"procesos con PID {pid} finalizado.")
    except psutil.NoSuchProcess as e:
        print(f"Error: {e}")
    except psutil.AccessDenied as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\nOpciones:")
        print("1. listado de todos los procesos")
        print("2. finalizar un proceso a traves de PID")
        print("3. Exit")

        choice = input("Elije una opcion (1/2/3): ")

        if choice == "1":
            listado_de_procesos()
        elif choice == "2":
            try:
                pid_to_terminate = int(input("Introduce el PID del proceso a terminar: "))
                Finalizar_proceso(pid_to_terminate)
            except ValueError:
                print("Entrada invalida. Introduzca un PID valido.")
        elif choice == "3":
            break
        else:
            print("Eleccion incorrecta. Elija entre 1, 2, o 3.")

if __name__ == "__main__":
    main()