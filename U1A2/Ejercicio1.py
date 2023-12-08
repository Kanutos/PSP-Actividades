"""Exercise 1: Using the multiprocessing module, write a simple python program as follows:

Create a pool of workers to run parallel tasks.
The pool size should be the number of CPU cores available on your node minus 1 (8cores > pool of 7 workers).
Write a function to be running in parallel, call it my_id. The function should receive as input the task id. When called, 
the function will print to the screen a message in the form: “Hi, I’m worker ID (with PID)” Where ID should be replaced with
 the task number assigned to the worker and PID with the process ID of the running worker.
Run tasks in parallel using the map function, for a total of tasks equal to twice the number of CPU cores in your node."""

import multiprocessing
import os


def my_id(id_tarea):
    id_proceso = os.getpid()
    print(f"Hi, I'm worker {id_tarea} (with PID {id_proceso})")

def main():
    # Get the number of CPU cores on the node
    num_cores = multiprocessing.cpu_count()

    # Set the pool size to be one less than the number of CPU cores
    Tamaño_pool = num_cores - 1

    # Creando el multiproceso
    with multiprocessing.Pool(processes=Tamaño_pool) as pool:

    # Generando las tareas para el numero de nucleos
        id_tareas = list(range(1, 2 * num_cores + 1))

    #Corriendo en paralelo on la funcion map
        pool.map(my_id, id_tareas)

if __name__ == "__main__":
    main()
