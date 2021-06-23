'''

RETO 4 (MISIÓNTIC 2022)
Nombre del reto: Programación de Entregas de Múltiples Medicamentos a Pacientes con
Enfermedades no Transmisibles
Autor: Javier Bayter

Descripción del reto:
En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para
erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos como
parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es el de
salud y bienestar y una de sus metas busca reducir en un tercio la mortalidad prematura
por enfermedades no transmisibles mediante la prevención y el tratamiento.
Debido a esto, el ministerio de salud desea que usted construya un sistema para la
programar la entrega de existencias de múltiples tipos de medicamentos en varias
sucursales de una IPS para el tratamiento y prevención de la hipoglucemia y la
diabetes, en pos del mejoramiento de la calidad de vida de los ciudadanos.
Para ello, el sistema debe recibir como entrada la cantidad de sucursales (n) para la
entrega de medicamentos seguido del número de diferentes tipos de medicamento (k) y
de la cantidad total de pacientes a atender (m), si la cantidad de sucursales es menor a
1 o si el número de diferentes tipos de medicamento es menor a 1 se debe leer
nuevamente todos los valores previamente mencionados hasta que se ingresen un n y
un k válidos.
Luego, para las n sucursales (numeradas de 1 a n) se debe leer la cantidad de
existencias actuales de todos los tipos de medicamentos en una línea. Finalmente, para
los m pacientes se debe leer el número de la sucursal donde será atendido, seguido del
tipo de medicamento solicitado y el número de existencias solicitadas del mismo,
seguido de una cadena de caracteres (“ayunas” o “posprandial”) que determina si el
paciente se encuentra o no en ayunas y de un número real que representa el nivel de
glucosa en sangre en mmol/dl.
Los rangos de valores de glucosa en sangre, y si se programa o no la entrega de
existencias se listan en la siguiente tabla:

¿En Ayunas?    Glucosa en Sangre(mmol/dl)   Categoría       ¿Se programa la entrega?
   ayunas             <0.44                hipoglusemia               Si
   ayunas          [0.44 - 0.61)             normal                   No
   ayunas          [0.61 - 0.7)              elevado                  Si
   ayunas            >=0.7                  diabetes                  Si
 posprandial          <0.78                  normal                   No
 posprandial       [0.78 - 1.1)              elevado                  Si
 posprandial         >=1.1                  diabetes                  Si

Si no se encuentra la categoría (valor distinto de “ayunas” y “posprandial” en ayunas)
del paciente o la sucursal donde será atendido el paciente no es válida o el tipo de
medicamento no es válido o la cantidad de dosis solicitadas es menor a 0, no se
programa la entrega ninguna existencia del medicamento y el paciente tampoco se
toma en cuenta en el conteo de pacientes por sucursal.

El programa debe mostrar por pantalla para cada una de las sucursales:
    * El número de la sucursal.
    * El número del tipo de medicamento con la menor cantidad de existencias luego
      de realizar la entrega de las existencias programadas, seguido de la cantidad
      antes mencionada.
    * El número del tipo de medicamento con la mayor cantidad de existencias luego
      de realizar la entrega de las existencias programadas, seguido de la cantidad
      antes mencionada.
    * La cantidad mínima, promedio y máxima de existencias programadas para
      entrega entre los k tipos de medicamento, formateado a 2 cifras decimales y
      separados por espacio.
    * El promedio de existencias programadas, independientemente del tipo, por
      paciente en la sucursal correspondiente, formateado a 2 cifras decimales y
      separados por espacio. Si la cantidad de pacientes atendidos en la sucursal es
      0, el promedio debe ser 0.00.

    Si hay más de un medicamento con iguales cantidades mínimas o máximas luego
    de hacer la entrega de las existencias programadas, se debe mostrar el que tenga
    el menor número.
    
Finalmente, se debe mostrar:
    * El número de la sucursal con la
      para entrega del medicamento
      mencionada.
    * El número de la sucursal con la
      para entrega del medicamento
      mencionada.
    Si hay más de una sucursal con iguales cantidades mínimas o máximas de la
    cantidad de existencias programadas del medicamento de tipo 1, se debe mostrar la
    que tenga menor número.
      
'''

#Inicialización: # Sucursales, # Diferentes tipos de medicamentos, # Pacientes a atender
n_k_m = [0,0,0]
#Ciclo para el control de n y k
while n_k_m[0]<1 or n_k_m[1]<1:
  #Entrada de sucursales y pacientes
  n_k_m = tuple([int(i) for i in input().split()])
        
#Matriz con existencias de medicamentos por sucursal   
k_n = tuple([tuple([int(j) for j in input().split()]) for i in range(n_k_m[0])])

#Inicialización de una nueva matriz de existencias por sucursal
k_n_new = [list(i) for i in k_n]
#Inicialización de contador de pacientes por sucursal
m_new = [0]*n_k_m[0]

#Ciclo para controlar el flujo de medicamentos
for _ in range(n_k_m[2]):
  #Entrada de información de cada paciente
  pacienteInfo = [i for i in input().split()]
  pacienteInfo[0:3] = list(map(int, pacienteInfo[0:3]))
  pacienteInfo[4] = float(pacienteInfo[4])
  #Condiciones para tener en cuenta el paciente
  condition1 = pacienteInfo[0] in range(1,n_k_m[0]+1)
  condition2 = pacienteInfo[1] in range(1,n_k_m[1]+1)
  condition3 = pacienteInfo[2]>=0
  condition4 = pacienteInfo[3] in ('ayunas','posprandial')
  if condition1 and condition2 and condition3 and condition4:
    m_new[pacienteInfo[0]-1] += 1
    if pacienteInfo[3] == 'ayunas':
      if pacienteInfo[4]<0.44:
        k_n_new[pacienteInfo[0]-1][pacienteInfo[1]-1] -= pacienteInfo[2]
      elif 0.61<=pacienteInfo[4]<0.7:
        k_n_new[pacienteInfo[0]-1][pacienteInfo[1]-1] -= pacienteInfo[2]
      elif pacienteInfo[4]>=0.7:
        k_n_new[pacienteInfo[0]-1][pacienteInfo[1]-1] -= pacienteInfo[2]
    elif pacienteInfo[3] == 'posprandial':
      if 0.78<=pacienteInfo[4]<1.1:
        k_n_new[pacienteInfo[0]-1][pacienteInfo[1]-1] -= pacienteInfo[2]
      elif pacienteInfo[4]>=1.1:
        k_n_new[pacienteInfo[0]-1][pacienteInfo[1]-1] -= pacienteInfo[2] 
        
#Matriz de existencias programadas      
existProg = [[k_n[i][j]-k_n_new[i][j] for j in range(len(k_n[i]))] for i in range(len(k_n))]

#Salidas
for i in range(n_k_m[0]):
  print(i+1) #Salida 1
  
  #Extraer Máximo y Minimo de las existencias y su posición
  maxExistencia = max(k_n_new[i])
  minExistencia = min(k_n_new[i])
  idxMax = k_n_new[i].index(maxExistencia)
  idxMin = k_n_new[i].index(minExistencia)
  
  print(f'{idxMin+1} {minExistencia}') #Salida 2
  print(f'{idxMax+1} {maxExistencia}') #Salida 3
  
  #Extraer Máximo y Minimo de las existencias programadas y su posición
  maxExistenciaProg = max(existProg[i])
  minExistenciaProg = min(existProg[i])
  #Promedio de existencias programadas
  promedioExisProg = sum(existProg[i])/n_k_m[1]
  
  print(f'{minExistenciaProg:.2f} {promedioExisProg:.2f} {maxExistenciaProg:.2f}') #Salida 4
  
  #Promedio de existencias programadas independientemente del tipo
  if m_new[i]!=0:
    promedioExisProgInd = sum(existProg[i])/m_new[i]
  else:
    promedioExisProgInd = 0
  
  print(f'{promedioExisProgInd:.2f}') #Salida 5 
  
#Lista de existencias programadas de medicamento tipo 1 por sucursal
existProgMed1 = tuple([list(i) for i in zip(*existProg)])[0]

#Extraer Sucursal con mayor y menor existencias programadas de med.tipo 1 
maxExistenciaMed1 = max(existProgMed1)
minExistenciaMed1 = min(existProgMed1)
idxMaxMed1 = existProgMed1.index(maxExistenciaMed1)
idxMinMed1 = existProgMed1.index(minExistenciaMed1)

print(f'{idxMinMed1+1} {minExistenciaMed1}') #Salida 6
print(f'{idxMaxMed1+1} {maxExistenciaMed1}') #Salida 7
  