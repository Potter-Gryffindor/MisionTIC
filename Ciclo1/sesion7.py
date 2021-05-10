"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

Por ejemplo:
"""

def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        i += 1
ejemplo1()

def actividad1():
    print("actividad1")
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número. 
    num = abs(int(input('Ingrese un número: ')))
    par = 2
    if num<par:
        print('El número debe ser mayor o igual a 2')
    while par<=num:
        print(par)
        par += 2 
    
actividad1()

def actividad2():
    print("actividad2")
    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.
    num = abs(int(input('Ingrese un número: ')))
    digitos = 1
    while num//10!=0:
        digitos += 1
        num //= 10
    print(f'# de digitos: {digitos}')

actividad2()    
    

def actividad3():
    print("actividad3")
    #Escribe el código que solicite números al usuario hasta que éste ingrese -1.
    #Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).
    num = 0
    n = 0
    suma = 0
    while num!=-1:
        num = float(input('Ingrese un número: '))
        if num!=-1:
            suma += num
            n += 1
    prom = suma/n if n!=0 else 0
    print(prom) 
    
actividad3()