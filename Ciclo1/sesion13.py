"""
Matrices o vectores bidimensionales

En Python podemos trabajar los arreglos bidimensionales como listas de listas, es decir, cada elemento de la lista es una lista.

Nota Existe una librería en Python que maneja tanto vectores como matrices llamada numpy. 
Esta librería está por fuera del alcance de este curso pero puedes investigarla.

Veamos un ejemplo:
"""
def ejemplo1():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    print(a)

#ejemplo1()

#O podemos recorrer todos los elementos e imprimir como una matriz
def ejemplo2():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

#ejemplo2()

#Actividad 1
#
#Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y 100
#aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.
def actividad1():
    import random
    matriz = [[random.randint(1,100) for j in range(10)] for i in range(5)]
    maximo, posMax = matriz[0][0], [0,0]
    minimo, posMin  = matriz[0][0], [0,0]
    print('Matriz:')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]>=maximo:
                maximo, posMax = matriz[i][j], [i,j]
            if matriz[i][j]<=minimo:
                minimo, posMin = matriz[i][j], [i,j]    
            print(matriz[i][j], end=' ')
        print('')
    print(f'Máximo{posMax}: {maximo}')
    print(f'Minimo{posMin}: {minimo}')    
         
#actividad1()

#Actividad 2

#El producto escalar de un número real, x , y una matriz A es la matriz xA. 
#Cada elemento de la matriz xA es x veces su elemento correspondiente en A.

#Diseñemos una funcion producEscalar(matriz, escalar) que dada matriz[n][m] y un escalar, 
#imprima el producto escalar de la matriz.
def producEscalar(matriz, escalar):
    newMatriz = [[escalar*matriz[i][j] for j in range(len(matriz[i]))] for i in range(len(matriz))]
    print(f'{escalar}*Matriz:')
    for i in range(len(newMatriz)):
        for j in range(len(newMatriz[i])):
            print(newMatriz[i][j], end=' ')
        print('')
def actividad2():
    filas = int(input('#Filas: '))
    columnas = int(input('#Columnas: '))
    matriz = [[float(input(f'Elemento[{i}][{j}]: ')) for j in range(columnas)] for i in range(filas)]
    escalar = int(input('Escalar: '))
    producEscalar(matriz, escalar)
#actividad2()