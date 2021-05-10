"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

La opción break, puede parar el ciclo aunque la condición sea real. Por ejemplo:
"""

def ejemplo1():
    print("ejemplo1")
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1 
ejemplo1()

def actividad1():
    print("actividad1")
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número pero que termine el proceso si llega al 10.
    num = abs(int(input('Ingrese un número: ')))
    par = 2
    if num<par:
        print('El número debe ser mayor o igual a 2')
    while par<=num:
        print(par)
        if par==10:
            break
        par += 2
        

actividad1()


"""
La opción continue, puede continuar el ciclo y saltarse cuando sea verdadera. Por ejemplo:
"""
def ejemplo2():
    print("ejemplo2")
    i = 1
    while i < 6:
        if i == 3:
            i += 1 
            continue
        print(i)
        i += 1 

ejemplo2()

def actividad2():
    print("actividad2")
    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario pero saltarse si el digito es 4.
    num = abs(int(input('Ingrese un número: ')))
    digitos = 1 if num%10!=4 else 0
    while num//10!=0:
        num //= 10
        if num%10!=4:
            digitos += 1
    print(f'# de digitos: {digitos}')

actividad2()