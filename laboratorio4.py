#!/usr/bin/python3

import random


class matriz:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matriz = []
        for fila in range(n):
            a = []
            for columna in range(m):
                a.append(0)
            self.matriz.append(a)

    def __str__(self):

        for i in self.matriz:
            for j in i:
                print(str(j), end=" ")
            print("\n")
        return ""

    def get(self, fila, columna):

        return self.matriz[fila-1][columna-1]

    def set(self, fila, columna, nuevo_valor):
        self.matriz[fila-1][columna-1] = nuevo_valor

        return self

    def __add__(self, other):

        try:
            nueva_matriz = matriz(self.n, self.m)
            for fila in range(self.n):

                for columna in range(self.m):
                    a = self.matriz[fila][columna]+other.matriz[fila][columna]
                    nueva_matriz.set(fila+1, columna+1, a)
            return nueva_matriz
        except IndexError:
            print("El tamaño de las matrices debe ser el mismo")

    def __sub__(self, other):
        if (len(self.matriz[0]) != len(other.matriz[0]) or
           len(self.matriz[1]) != len(other.matriz[1])):
            raise ValueError("Las matrices deben ser del mismo tamaño")
        else:
            nueva_matriz = matriz(self.n, self.m)
            for fila in range(self.n):

                for columna in range(self.m):
                    a = self.matriz[fila][columna]-other.matriz[fila][columna]
                    nueva_matriz.set(fila+1, columna+1, a)
            return nueva_matriz

    def size(self):
        return[self.n, self.m]

    def randm(self):
        random_matrix = matriz(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                a = random.randint(0, 9)
                random_matrix.set(i+1, j+1, a)
        return random_matrix


# Programa de prueba

matriz_a = matriz(4, 4)
matriz_b = matriz(4, 4)
matriz_c = matriz(3, 4)
print(
      "Las entradas de la matriz a son:\n", (matriz_a),
      "Las entradas de la matriz b son:\n", (matriz_b),
      "Las entradas de la matriz c son:\n", (matriz_c)
      )

# se agregan valores al azar a las entradas de las matrices del 0 al 9

matriz_a = matriz_a.randm()
matriz_b = matriz_b.randm()
matriz_c = matriz_c.randm()

print(
      "Se han agregado valores aleatorios del 0 al 9 a las"
      "entradas de las matrices "
      "para la comprobación de las funciones\n",
      "\nLas nuevas entradas de la matriz a son:\n", (matriz_a),
      "Las nuevas entradas de la matriz b son:\n", (matriz_b),
      "Las nuevas entradas de la matriz c son:\n", (matriz_c)
      )
# Comprobacion de los métodos set y get

matriz_c = matriz_c.set(2, 1, 8)

print(" La nueva matriz c con la entrada (2,1) cambiada es:\n", matriz_c)

entrada21 = matriz_c.get(2, 1)

print("EL valor de la entrada(2, 1) de la matriz c es {}\n \n".format(entrada21))

# Comprabaión de los método de suma, resta y error por diferencia de tamaño

matriz_d = matriz_a + matriz_b
print("La suma de la matriz a y b es:\n", matriz_d)

matriz_e = matriz_a - matriz_b

print("La resta de la matriz a y b es:\n", matriz_e)

print("Al intentar sumar o restar las matrices a y c, de diferente tamaño"
      " matrices de diferente tamaño se obtiene el "
      "siguiente error:\n")
error = matriz_a+matriz_c
