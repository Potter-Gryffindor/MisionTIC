'''

RETO 5 (MISIÓNTIC 2022)
Nombre del reto: Programación de Entregas de Múltiples Medicamentos a
Pacientes con Enfermedades no Transmisibles
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

Para ello, el sistema debe leer la información del archivo data.csv, que contiene los
siguientes campos / columnas:

    * first_name: El primer nombre del paciente.
    * last_name: El primer apellido del paciente.
    * gender: El género del paciente (‘m’ para hombres o ‘f’ para mujeres).
    * city_name: El nombre de la cuidad donde se encuentra la sucursal.
    * department_name: El nombre del departamento donde se encuentra la
      sucursal.
    * id_branch: El número identificador de la sucursal (entre 1 y 32).
    * medicine_type: El tipo de medicamento que la persona está solicitando (entre 1
      y 20).
    * medicine_quantity: Cantidad de existencias que el paciente está solicitando.
    * fasting: Determina si el paciente se encuentra o no en ayunas (‘ayunas’ o
      ‘posprandial’).
    * glucose: El valor del nivel de glucosa en sangre.

Una sucursal solo se encuentra en una única ciudad y en un único departamento.

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
 
Adicionalmente, se debe recibir como entrada varios números identificadores de
distintas sucursales.

El programa debe mostrar por pantalla para cada una de las sucursales leídas
previamente, en orden ascendente, la siguiente información haciendo uso de los datos
del archivo data.csv:
* El número identificador de la sucursal, el nombre de la ciudad y el nombre del
  departamento donde se encuentra la sucursal.
* La cadena ‘patients’.
* La cadena ‘male’, seguido de la cantidad de hombres que solicitaron
  medicamentos en esa sucursal.
* La cadena ‘female’, seguido de la cantidad de mujeres que solicitaron
  medicamentos en esa sucursal.
* La cadena ‘total’, seguido de la cantidad de total de pacientes que solicitaron
  medicamentos en esa sucursal.
* La cadena ‘medicine quantity’.
* La cadena ‘mean’, seguido de la media (promedio) de la cantidad de
  medicamentos solicitados, independientemente del tipo, en esa sucursal,
  formateado a 2 cifras decimales.
* La cadena ‘std’, seguido de la desviación estándar muestral de la cantidad de
  medicamentos solicitados, independientemente del tipo, en esa sucursal,
  formateado a 2 cifras decimales.
* La cadena ‘min’, seguido de la cantidad mínima de medicamentos solicitados,
  independientemente del tipo.
* La cadena ‘max’, seguido de la cantidad máxima de medicamentos solicitados,
  independientemente del tipo.
* La cadena ‘total’, seguido del total de medicamentos solicitados,
  independientemente del tipo.
* La cadena ‘scheduled patients’.
* La cadena ‘male’, seguido de la cantidad de hombres a los que se les programa
  la entrega medicamentos en esa sucursal.
* La cadena ‘female’, seguido de la cantidad de mujeres a las que se les
  programa la entrega medicamentos en esa sucursal.
* La cadena ‘total’, seguido de la cantidad de total de pacientes a los que se les
  programa la entrega medicamentos en esa sucursal.
* La cadena ‘scheduled medicine quantity’.
* La cadena ‘mean’, seguido de la media (promedio) de la cantidad de
  medicamentos programados para entrega, independientemente del tipo, en esa
  sucursal, formateado a 2 cifras decimales.
* La cadena ‘std’, seguido de la desviación estándar muestral de la cantidad de
  medicamentos programados para entrega, independientemente del tipo, en esa
  sucursal, formateado a 2 cifras decimales.
* La cadena ‘min’, seguido de la cantidad mínima de medicamentos programados
  para entrega (independientemente del tipo), el nombre completo (nombre y
  apellido) del paciente al que se le haya programado esta cantidad, su género y
  el tipo de medicamento que se programó. Si hay más de un paciente, se toma la
  información del primero que se encuentre.
* La cadena ‘max’, seguido de la cantidad máxima de medicamentos
  programados para entrega (independientemente del tipo), el nombre completo
  (nombre y apellido) del paciente al que se le haya programado esta cantidad, su
  género y el tipo de medicamento que se programó. Si hay más de un paciente,
  se toma la información del primero que se encuentre.
* La cadena ‘total’, seguido del total de medicamentos programados para entrega,
  independientemente del tipo.
'''
import csv
import statistics as st

#Inicialización del diccionario de los datos
rows = {}
rows['first_name'],rows['last_name'] = [],[]
rows['gender'],rows['city_name'] = [],[]
rows['department_name'],rows['id_branch'] = [],[]
rows['medicine_type'],rows['medicine_quantity'] = [],[]
rows['fasting'],rows['glucose'] = [],[]

#Se abre el archivo y se asigna a un diccionario
with open('data.csv', encoding='utf-8',newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    for key,value in row.items():
      if key in ('id_branch','medicine_type','medicine_quantity'):
        rows[key].append(int(row[key]))
      elif key == 'glucose':
        rows[key].append(float(row[key]))
      else:
        rows[key].append(row[key])
#Conversión a tupla de los elementos del diccionario
for key,value in rows.items():
  rows[key] = tuple(rows[key])

#Entrada 
sucursales = [int(i) for i in input().split()]
sucursales = tuple(sorted(sucursales))

for i in sucursales:
  index = rows['id_branch'].index(i)
  id_branch = i
  city_name = rows['city_name'][index]
  department_name = rows['department_name'][index]
  print(f'{id_branch} {city_name} {department_name}') #Salida 1
  print('patients') #Salida 2
  
  #Ciclo que suma la cantidad de hombres y mujeres solicitantes en la sucursal
  sumMF_sucursal = [0,0]
  for j in range(len(rows['gender'])):
    if rows['gender'][j]=='m' and rows['id_branch'][j]==i:
      sumMF_sucursal[0] += 1
    elif rows['gender'][j]=='f' and rows['id_branch'][j]==i:
      sumMF_sucursal[1] += 1
  
  print(f'male {sumMF_sucursal[0]}') #Salida 3
  print(f'female {sumMF_sucursal[1]}') #Salida 4
  print(f'total {sum(sumMF_sucursal)}') #Salida 5
  
  print('medicine quantity') #Salida 6
  
  #Cálculos de la media y desviación estandar
  medicine_quantity = tuple([rows['medicine_quantity'][k] for k in range(len(rows['medicine_quantity'])) if rows['id_branch'][k]==i]) 
  promedio = st.mean(medicine_quantity) #Media
  desvision_std = st.stdev(medicine_quantity) #Desviasión estandar
  
  print(f'mean {promedio:.2f}') #Salida 7
  print(f'std {desvision_std:.2f}') #Salida 8
  
  #Minimo y máximo de medicamentos solicitados
  maxMed = max(medicine_quantity)
  minMed = min(medicine_quantity)
  
  print(f'min {minMed}') #Salida 10
  print(f'max {maxMed}') #Salida 11
  
  #Total de medicamentos solicitados
  totalMed = sum(medicine_quantity)
  
  print(f'total {totalMed}') #Salida 12
  
  print('scheduled patients') #Salida 13
  
  sumMF_Progsucursal = [0,0]
  newMedicineQuantity = [] #Vector con cantidades programadas
  
  #Inicialización de valores minimos y máximos de medicinas programadas
  minMedProg,maxMedProg = None,None
  #Ciclo que suma la cantidad de hombres y mujeres programados en la sucursal
  for j in range(len(rows['gender'])):
    if rows['id_branch'][j]==i:
      switch1,switch2 = 0,0
      if rows['gender'][j]=='m':
        indice = 0
      elif rows['gender'][j]=='f':
        indice = 1
      if rows['fasting'][j] == 'ayunas':
        if rows['glucose'][j]<0.44:
          sumMF_Progsucursal[indice] += 1
          newMedicineQuantity.append(rows['medicine_quantity'][j])
          if minMedProg==None or rows['medicine_quantity'][j]<minMedProg:
            switch1 = 1
          if maxMedProg==None or rows['medicine_quantity'][j]>maxMedProg:
            switch2 = 1
        elif 0.61<=rows['glucose'][j]<0.7:
          sumMF_Progsucursal[indice] += 1
          newMedicineQuantity.append(rows['medicine_quantity'][j])
          if minMedProg==None or rows['medicine_quantity'][j]<minMedProg:
            switch1 = 1
          if maxMedProg==None or rows['medicine_quantity'][j]>maxMedProg:
            switch2 = 1
        elif rows['glucose'][j]>=0.7:
          sumMF_Progsucursal[indice] += 1
          newMedicineQuantity.append(rows['medicine_quantity'][j])
          if minMedProg==None or rows['medicine_quantity'][j]<minMedProg:
            switch1 = 1
          if maxMedProg==None or rows['medicine_quantity'][j]>maxMedProg:
            switch2 = 1
      elif rows['fasting'][j] == 'posprandial':
        if 0.78<=rows['glucose'][j]<1.1:
          sumMF_Progsucursal[indice] += 1
          newMedicineQuantity.append(rows['medicine_quantity'][j])
          if minMedProg==None or rows['medicine_quantity'][j]<minMedProg:
            switch1 = 1
          if maxMedProg==None or rows['medicine_quantity'][j]>maxMedProg:
            switch2 = 1
        elif rows['glucose'][j]>=1.1:
          sumMF_Progsucursal[indice] += 1
          newMedicineQuantity.append(rows['medicine_quantity'][j])
          if minMedProg==None or rows['medicine_quantity'][j]<minMedProg:
            switch1 = 1
          if maxMedProg==None or rows['medicine_quantity'][j]>maxMedProg:
            switch2 = 1
      
      #Condicionales para actualizar valores minimos y máximos
      if switch1==1:
        minMedProg = rows['medicine_quantity'][j]
        nombreMin = rows['first_name'][j]
        apellidoMin = rows['last_name'][j]
        genMin = rows['gender'][j]
        medTipeMin = rows['medicine_type'][j]
      if switch2==1:
        maxMedProg = rows['medicine_quantity'][j]
        nombreMax = rows['first_name'][j]
        apellidoMax = rows['last_name'][j]
        genMax = rows['gender'][j]
        medTipeMax = rows['medicine_type'][j]
  
  print(f'male {sumMF_Progsucursal[0]}') #Salida 14
  print(f'female {sumMF_Progsucursal[1]}') #Salida 15
  print(f'total {sum(sumMF_Progsucursal)}') #Salida 16
    
  print('scheduled medicine quantity') #Salida 17
    
  #Cálculos de la media y desviación estandar de las medicinas programadas
  promedioProg = st.mean(newMedicineQuantity) #Media
  desvision_stdProg = st.stdev(newMedicineQuantity) #Desviasión estandar
    
  print(f'mean {promedioProg:.2f}') #Salida 18
  print(f'std {desvision_stdProg:.2f}') #Salida 19
    
  print(f'min {minMedProg} {nombreMin} {apellidoMin} {genMin} {medTipeMin}')  #Salida 20
  print(f'max {maxMedProg} {nombreMax} {apellidoMax} {genMax} {medTipeMax}')  #Salida 21
  print(f'total {sum(newMedicineQuantity)}') #Salida 22
  