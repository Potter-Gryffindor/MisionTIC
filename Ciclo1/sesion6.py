# Diseñar 3 funciones:
#
#   1. Leer un número de 4 dígitos, mostrar el dígito mayor e 
#      informar si es par o impar.
#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
#      con el mayor del primero y el menor del segundo.
#   3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.
#   
# Crea la función principal como un menú con las tres opciones.

def funcion1():
    #La función abs evita el problema si el usuario digita un número negativo
    numero = abs(int(input('Ingrese un número de 4 digitos: ')))

    #Se descompone el número en sus cifras
    unidad = numero%10
    decena = (numero//10)%10
    centena = (numero//100)%10
    unidadDeMil = (numero//1000)%10

    #Condicional para extraer el dígito mayor
    if unidad>=decena and unidad>=centena and unidad>=unidadDeMil:
        mayor = unidad
    elif decena>=unidad and decena>=centena and decena>=unidadDeMil:
        mayor = decena 
    elif centena>=unidad and centena>=decena and centena>=unidadDeMil:
        mayor = centena
    elif unidadDeMil>=unidad and unidadDeMil>=decena and unidadDeMil>=centena:
        mayor = unidadDeMil

    #Condicionar para verificar si la cifra mayor es par
    if mayor%2==0:
        par = 'si'
    else:
        par = 'no'

    print(f'El digito mayor es {mayor}, además {par} es par.')
    

def funcion2():
    #La función abs evita el problema si el usuario digita un número negativo
    numero1 = abs(int(input('Ingrese el primer número de 3 digitos: ')))
    numero2 = abs(int(input('Ingrese el segundo número de 3 digitos: ')))
    
    #Se descompone el número1 y numero2 en sus cifras
    unidad1,unidad2 = numero1%10,numero2%10 
    decena1,decena2 = (numero1//10)%10,(numero2//10)%10
    centena1,centena2 = (numero1//100)%10,(numero2//100)%10

    #Condicional para extraer el dígito mayor del número1
    if (unidad1>=decena1 and unidad1>=centena1):
        mayor1 = unidad1
    elif (decena1>=unidad1 and decena1>=centena1):
        mayor1 = decena1
    elif (centena1>=unidad1 and centena1>=decena1):
        mayor1 = centena1
    
    #Condicional para extraer el dígito menor del número2
    if (unidad2<=decena2 and unidad2<=centena2):
        menor2 = unidad2
    elif (decena2<=unidad2 and decena2<=centena2):
        menor2 = decena2
    elif (centena2<=unidad2 and centena2<=decena2):
        menor2 = centena2
    
    #Formar e imprimir número compuesto por el mayor del primero y el menor del segundo
    numero3 = str(mayor1)+str(menor2)
    print(f'El número formado es: {numero3}')
    

def funcion3():
    #La función abs evita el problema si el usuario digita un número negativo
    numero = abs(int(input('Ingrese un número de 3 digitos: ')))
        
    #Se descompone el número1 
    unidad = numero%10
    decena = (numero//10)%10
    centena = (numero//100)%10

    #Se declaran las 6 formas posibles en que se pueden ordenar
    forma1 = int(str(centena)+str(decena)+str(unidad))
    forma2 = int(str(centena)+str(unidad)+str(decena))
    forma3 = int(str(unidad)+str(decena)+str(centena))
    forma4 = int(str(unidad)+str(centena)+str(decena))
    forma5 = int(str(decena)+str(centena)+str(unidad))
    forma6 = int(str(decena)+str(unidad)+str(centena))

    #Se comparan los 6 números entre ellos
    if forma1>=forma2 and forma1>=forma3 and forma1>=forma4 and forma1>=forma5 and forma1>=forma6:
        mayor = forma1
    elif forma2>=forma3 and forma2>=forma4 and forma2>=forma5 and forma2>=forma6:
        mayor = forma2
    elif forma3>=forma4 and forma3>=forma5 and forma3>=forma6:
        mayor = forma3
    elif forma4>=forma5 and forma4>=forma6:
        mayor = forma4 
    elif forma5>=forma6:
        mayor = forma5
    else:
        mayor = forma6 

    print(f'El mayor número formado con las cifras de {numero} es: {mayor}')   

if __name__ == "__main__":
    funcion1()
    funcion2()
    funcion3()
