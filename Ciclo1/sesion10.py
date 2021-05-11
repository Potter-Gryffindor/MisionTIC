"""
Funciones

    La verdad es que hemos venido trabajando con funciones desde que empezamos con archivos .py 
    En Python, definimos una función con la siguiente estructura

    def funcion(parametros)

    Recuerda que los parametros son opcionales!
"""

def suma(a,b):
    
    print(a+b)

#suma(3,4)

'''
Actividad 1
    Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los 
    productos de su cliente, su precio y calcular el total a pagar.

    Diseña un programa con las siguiente características:

        1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
        2. Una variable total que vaya sumando el precio de los artículos
        3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
        el precio de cada producto y los imprima.
        4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más 
        artículos a ingresar. Si no tiene, el programa debe detenerse.
        5. Si no hay más artículos, que imprima el total de la compra

        Al final de tus funciones, puedes simplemente llamar a la función caja para probar
'''
def imprimaProducto(nombre, precio):
    print(f'{nombre}: {precio}')
def caja():
    print('Actividad 1')
    total = 0
    while True:
        nombre = input('Nombre del producto: ')
        precio = float(input('Precio: '))
        imprimaProducto(nombre,precio)
        switch = input('¿Tiene más articulos a ingresar? [Si|No]: ')
        total += precio
        if switch == 'No':
            print(f'Total de la compra: {total}')
            break
#caja()

'''
Actividad 2

    Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
    excepto los números 110, 115 y 120 .

    Adicionalmente, una función numeros que imprima diez números aleatorios 
    (retornados por la función numAleatorio()) alternando par, impar, comenzando por par.
'''
def numAleatorio():
    import random
    while True:
        numero = random.randint(100,130)
        if not(numero in (110,115,120)):
            break
    return numero
def numeros():
    for i in range(10):
        while True:
            numero = numAleatorio()
            if (numero%2==0 and i%2==0) or (numero%2!=0 and i%2!=0):
                break
        print(numero)
#numeros()