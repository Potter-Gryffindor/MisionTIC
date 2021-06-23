'''

RETO 3 (MISIÓNTIC 2022)
Nombre del reto: Programación de Entregas de Medicamentos a Pacientes con
Enfermedades no Transmisibles
Autor: Javier Bayter

Descripción del reto:
En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para
erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos como
parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es el de
salud y bienestar y una de sus metas busca reducir en un tercio la mortalidad prematura
por enfermedades no transmisibles mediante la prevención y el tratamiento.
Debido a esto, el ministerio de salud desea que usted construya un sistema para la
programar la entrega de existencias de un tipo de medicamento en varias sucursales de
una IPS para el tratamiento y prevención de la hipoglucemia y la diabetes, en pos del
mejoramiento de la calidad de vida de los ciudadanos.
Para ello, el sistema debe recibir como entrada la cantidad de sucursales (n) para la
entrega de medicamentos seguido de la cantidad total de pacientes a atender (m), si la
cantidad de sucursales es menor a 1 se debe leer nuevamente ambos valores hasta
que se ingrese un n válido. Luego, para las n sucursales (numeradas de 1 a n) se debe
leer la cantidad de existencias actuales del medicamento y esta debe ser mayor o igual
a 1, y en caso de que no se cumpla se debe leer valores hasta que se ingrese uno
válido. Finalmente, para los m pacientes se debe leer el número de la sucursal donde
será atendido, seguido de una cadena de caracteres (“ayunas” o “posprandial”) que
determina si el paciente se encuentra o no en ayunas y de un número real que
representa el nivel de glucosa en sangre en mmol/dl.
Los rangos de valores de glucosa en sangre, así como su categoría y la cantidad y tipo
de medicamento entregado se listan en la siguiente tabla:

¿En Ayunas?    Glucosa.Sangre(mmol/dl)      Categoría       Tipo. medicamento   #Dosis
   ayunas             <0.44                hipoglusemia            1               4
   ayunas          [0.44 - 0.61)             normal             Ninguno            0
   ayunas          [0.61 - 0.7)              elevado               1               6
   ayunas            >=0.7                  diabetes               1               12
 posprandial          <0.78                  normal             Ninguno            0
 posprandial       [0.78 - 1.1)              elevado               1               9
 posprandial         >=1.1                  diabetes               1               18

Si no se encuentra la categoría (valor distinto de “ayunas” y “posprandial” en ayunas)
del paciente o la sucursal donde será atendido el paciente no es válida, no se programa
la entrega ninguna existencia del medicamento.
El programa debe mostrar por pantalla el número de la sucursal con la menor cantidad
de existencias, luego de realizar la entrega de las mismas, seguido de la cantidad antes
mencionada. Luego, en una nueva línea se debe mostrar el número de la sucursal con
la mayor cantidad de existencias, luego de realizar la entrega de las mismas, seguido
de la cantidad antes mencionada. Finalmente, para cada una de las sucursales (en
orden ascendente por número y en líneas distintas) se debe mostrar su número seguido
de la proporción porcentual de las existencias del medicamento programadas para
entrega respecto a la cantidad de existencias actuales del medicamento en la sucursal
correspondiente, formateado a 2 cifras decimales y separado por espacio.
Si hay más de una sucursal con iguales cantidades mínimas o máximas, se debe
mostrar la que tenga menor número.

'''

#Inicialización del número de sucursales y pacientes
numSucursales_numPacientes = [0,0] 
#Ciclo para el control del número de sucursales >1
while numSucursales_numPacientes[0]<1:
    #Entrada de sucursales y pacientes
    numSucursales_numPacientes = [int(i) for i in input().split()]
        
#Inicialización de arreglo con las existencias    
existencias = []
for _ in range(numSucursales_numPacientes[0]):
    existencia = 0 
    while existencia<1:
        existencia = int(input())
    existencias.append(existencia)

#Inicialización de arreglo con información de pacientes 
pacientesInfo = []
#Inicialización de un nuevo vector de existencias
nuevasExistencias = []
nuevasExistencias.extend(existencias)

#Ciclo para controlar el flujo de medicamentos
for _ in range(numSucursales_numPacientes[1]):
    #Entrada de información de cada paciente
    pacienteInfo = [i for i in input().split()] 
    pacienteInfo = [int(pacienteInfo[0]),pacienteInfo[1],float(pacienteInfo[2])]
    if pacienteInfo[1] == 'ayunas':
        if pacienteInfo[2]<0.44:
            nuevasExistencias[pacienteInfo[0]-1] -= 4
        elif 0.61<=pacienteInfo[2]<0.7:
            nuevasExistencias[pacienteInfo[0]-1] -= 6
        elif pacienteInfo[2]>=0.7:
            nuevasExistencias[pacienteInfo[0]-1] -= 12
    elif pacienteInfo[1] == 'posprandial':
        if 0.78<=pacienteInfo[2]<1.1:
            nuevasExistencias[pacienteInfo[0]-1] -= 9
        elif pacienteInfo[2]>=1.1:
            nuevasExistencias[pacienteInfo[0]-1] -= 18

#Extraer Máximo y Minimo de las existencias y su posición
maxExistencia = max(nuevasExistencias)
minExistencia = min(nuevasExistencias)
idxMax = nuevasExistencias.index(maxExistencia)
idxMin = nuevasExistencias.index(minExistencia)

#Salidas
print(idxMin+1,minExistencia)
print(idxMax+1,maxExistencia)
#Ciclo para el cálculo de porcentajes de existencias
for i in range(numSucursales_numPacientes[0]):
    porcentajeExistencias = 100*(existencias[i]-nuevasExistencias[i])/existencias[i]
    print(f'{i+1} {porcentajeExistencias:.2f}%')
