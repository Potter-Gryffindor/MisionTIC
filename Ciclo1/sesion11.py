"""
Vectores/Listas

Como vimos en la parte teórica, los vectores son una estructura de datos organizada que nos permite 
almacenar información. Una de las implementaciones más utilizadas es Python son las listas (List). 

Nota: En Python hay algunas diferencias menores entre un arreglo (array) y una lista, 
pero por ahora vamos a asumir que son lo mismo.

Vamos a ver una definición de esta estructura en Python. Para crear una lista, utilizamos los corchetes 
y separamos los valores de nuestra estructura con una coma. 

Por ejemplo, en la siguiente instrucción estamos creando una lista llamada a con los valores 1, 3, 2, 5, 2.
"""

def ejemplo1():
    a = [1, 3, 2, 5, 2]
    print(a)

#ejemplo1()

#Las listas no necesariamente tienen que ser de números, también pueden ser de texto:
def ejemplo2():
    nombres = ["María", "Juan","Andrés"]
    print(nombres)

#ejemplo2()

#Aquí van algunas funciones útiles cuando trabajamos con listas.
#    append(x) - inserta un nuevo valor x al final de la lista
#    remove(x) - remueve el primer valor X de la lista
#    pop([i]) - remueve el valor en la posición i. pop() remueve el último valor de la lista
#    len(x) - permite calcular el tamaño de una lista
#
# Ahora, veamoslas en acción
def ejemplo3():
    nombres = ["María", "Juan","Andrés"]
    nombres.append("Jorge")
    print(nombres)
    print(len(nombres))

    nombres.remove("Juan")
    print(nombres)
    print(len(nombres))

    nombres.pop(2)
    print(nombres)
    print(len(nombres))
#ejemplo3()

#Actividad 1

# Usando el conocimiento de ciclos, crea una funcion numeros que tenga una lista con los numeros pares del 1 al 10 
# y usa un ciclo para que los imprima
def actividad1():
    lista = [2, 4, 6, 8, 10]
    for numero in lista:
        print(numero,end=' ')
   
#actividad1()

#Actividad 2

#Escribamos un programa que nos permita crear una lista de 6 números aleatorios entre 1 y 20 en Python, y 
#creemos dos funciones que reciban la lista como parámetro de la siguiente forma:

#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos
def mayor(numeros):
    numMayor = numeros[0]
    for numero in numeros:
        if numero>=numMayor:
            numMayor = numero
    print(f'Mayor: {numMayor}')
    
def primos(numeros):
    listaPrimos = [numero for numero in numeros if 0 not in [numero%i for i in range(2,numero)] or numero==1]
    print(f'Primos: {listaPrimos}')

def actividad2():
    import random
    lista = [random.randint(1,20) for _ in range(6)]
    print(f'Lista: {lista}')
    mayor(lista)
    primos(lista)
          
actividad2()