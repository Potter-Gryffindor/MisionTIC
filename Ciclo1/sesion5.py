"""
Cada ejemplo y actividad será definida como una función independiente. La función principal será definida
al final del archivo.
Si-Sino-Finsi
Recuerda que los condicionales múltiples y anidados nos permiten evaluar múltiples casos. 
El condicional Si-Sino-Si-Finsi tiene la siguiente estructura:

    Si (condición) Entonces
        instrucción(es)
    Sino Si
        instrucción(es)
    Fin Si

En Python, esto se escribe un poco diferente y la estructura general depende de las tabulaciones. 
Por ejemplo:
"""
#EJEMPLO 1:
def ejemplo1():
    x = int(input("Por favor ingresa un número: "))
    if x < 0:
        print('El número es Negativo')
    elif x > 0:
        print('El número es positivo')
    elif x == 0:
        print('El número es cero')

#EJERCICIO 1:
#Escribe el código que imprima un comando dada la luz del semáforo
        #Verde = Siga
        #Amarillo = Precaución
        #Rojo = Pare
def actividad1(luz):
    if  luz == 'Verde':
        instruccion = 'Siga'
    elif luz == 'Amarillo':
        instruccion = 'Precaución'
    elif luz == 'Rojo':
        instruccion = 'Pare'
    
    print(instruccion)

#EJERCICIO 2:
#Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peatón o no (hayPeaton), imprima:
    #Verde -------- Si hay peaton - Pare, Sino - Siga
    #Amarillo ----------- Si hay peatón - Pare, Sino - Precaución
    #Rojo = Pare
def actividad2(luz, hayPeaton):
    if luz == 'Verde':
        if hayPeaton == True:
            instruccion = 'Pare'
        else:
            instruccion = 'Siga'
    elif luz == 'Amarillo':
        if hayPeaton == True:
            instruccion = 'Pare'
        else:
            instruccion = 'Precaución'
    elif luz == 'Rojo':
        instruccion = 'Pare'
    
    print(instruccion)

#EJERCICIO 3:
#Escribe el código para dos números a y b, el usuario va a seleccionar una opción: 
    #1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y 
    #retornar el resultado de la operación indicada.
def actividad3(a, b, opcion):
    if opcion == 1:
        print(a + b)
    elif opcion == 2:
        print(a*b)
    elif opcion == 3:
        print(a-b)
    elif opcion == 4:
        print(a/b)         

if __name__ == "__main__":
    ejemplo1()
    actividad1("Amarillo")
    actividad2("Verde", True)
    actividad3(4,2,4)