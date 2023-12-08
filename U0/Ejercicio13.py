# Ejercicio 13: Implementa la clase “Matriz” con los atributos int rows, int columns e int[rows][columns] matrix, que contenga los siguientes métodos: 
#      - getNumberRows(): devuelve el número de filas de la matriz.
#      - getNumberColumns(): devuelve el número de columnas de la matriz.
#      - setElement(int x, int j, int element): cambia el valor de la matriz en [x][j] por el valor de [element].
#      - addMatrix(int[][] matrix): suma todos los elementos de la matriz actual a los elementos de [matrix], y el resultado se almacena en la matriz inicial.
#        Si [matrix] no tiene el mismo número de filas y columnas que la matriz inicial, la operación no se puede realizar (notificalo).
#      - multMatrix(int[][] matrix]: multiplica todos los elementos de la matriz actual a los elementos de [matrix], y el resultado se almacena en la matriz inicial. 
#        Si [matrix] no tiene el mismo número de filas y columnas que la matriz inicial, la operación no se puede realizar (notificalo).

class Matriz:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0] * columns for _ in range(rows)]

    def getNumberRows(self):
        return self.rows

    def getNumberColumns(self):
        return self.columns

    def setElement(self, x, j, element):
        if 0 <= x < self.rows and 0 <= j < self.columns:
            self.matrix[x][j] = element

    def addMatrix(self, matrix):
        if len(matrix) == self.rows and len(matrix[0]) == self.columns:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] += matrix[i][j]
        else:
            print("No se puede realizar la suma de matrices. Tamaños incompatibles.")

    def multMatrix(self, matrix):
        if len(matrix) == self.rows and len(matrix[0]) == self.columns:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] *= matrix[i][j]
        else:
            print("No se puede realizar la multiplicación de matrices. Tamaños incompatibles.")

    def displayMatrix(self):
        for row in self.matrix:
            print(row)

# Ejemplo de uso de la clase Matriz
matriz1 = Matriz(2, 2)
matriz1.setElement(0, 0, 2)
matriz1.setElement(0, 1, 3)
matriz1.setElement(1, 0, 4)
matriz1.setElement(1, 1, 5)

matriz2 = Matriz(2, 2)
matriz2.setElement(0, 0, 1)
matriz2.setElement(0, 1, 1)
matriz2.setElement(1, 0, 1)
matriz2.setElement(1, 1, 1)

print("Matriz 1:")
matriz1.displayMatrix()

print("Matriz 2:")
matriz2.displayMatrix()

matriz1.addMatrix(matriz2)
print("Matriz 1 después de la suma:")
matriz1.displayMatrix()

matriz1.multMatrix(matriz2)
print("Matriz 1 después de la multiplicación:")
matriz1.displayMatrix()
