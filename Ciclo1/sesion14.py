"""
Matrices o vectores bidimensionales

Vamos a continuar con el trabajo de matrices usando lista de listas. 
Como vimos en la sesión anterior, las operaciones de este tipo de matrices se pueden realizar con ciclos anidados.
"""

#Actividad 1

#Escribe una función actividad1(x) que imprima la diagonal principal de una matriz x. 
#Asegúrate de validar si la matriz es cuadrada, sino devuelve un mensaje, "La matriz no es cuadrada"
def actividad1(matriz):
    switch = True
    for i in range(len(matriz)):
        if len(matriz)!=len(matriz[i]):
            switch = False
    if switch:
        diagonal = [matriz[i][i] for i in range(len(matriz))] 
        print(f'Diagonal: {diagonal}')
    else:
        print('La matriz no es cuadrada')      

#actividad1([[1,1,1],[2,7,2],[3,3,3]])


#Actividad 2

#Creemos ahora una función actividad2() que reciba los elementos de una matriz 3x3 e imprima:
#   - La primera fila
#   - La primera columna
#   - Accede al elemento en la fila 1, columna 1.
#Los valores son ingresados por filas [0][1], [0][2], [0][3], [1][0], etc
def actividad2():
    matriz = [[float(input(f'Elemento[{i}][{j}]: ')) for j in range(3)] for i in range(3)]
    fila0 = matriz[0]
    columna0 = [fila[0] for fila in matriz]
    print(f'Primera Fila: {fila0}')    
    print(f'Primera Columna: {columna0}')
    print(f'Elemento[1][1] = {matriz[1][1]}') 

#actividad2()