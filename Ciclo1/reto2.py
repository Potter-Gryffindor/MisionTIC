'''

RETO 2 (MISIÓNTIC 2022)
Nombre del reto: Entrega de Medicamentos a Pacientes con Enfermedades no
Transmisibles
Autor: Javier Bayter

Descripción del reto:
En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para
erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos como
parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es el de
salud y bienestar y una de sus metas busca reducir en un tercio la mortalidad prematura
por enfermedades no transmisibles mediante la prevención y el tratamiento.
Debido a esto, el ministerio de salud desea que usted construya un sistema para la
entrega de 2 tipos de medicamentos en una IPS para el tratamiento y prevención de la
hipoglucemia y la diabetes, en pos del mejoramiento de la calidad de vida de los
ciudadanos.
Para ello, el sistema debe recibir como entrada la cantidad de existencias del
medicamento 1 seguido de la cantidad de existencias del medicamento 2. Luego se
deberá leer una cadena de caracteres (“ayunas” o “posprandial”) que determina si el
paciente se encuentra o no en ayunas, seguido de un número real que representa el
nivel de glucosa en sangre en mmol/dl de múltiples pacientes y realizar la deducción de
los medicamentos entregados hasta que se acaben o se deban existencias de uno de
los 2 medicamentos.
Los rangos de valores de glucosa en sangre, así como su categoría y la cantidad y tipo
de medicamento entregado se listan en la siguiente tabla:

¿En Ayunas?    Glucosa.Sangre(mmol/dl)      Categoría       Tipo. medicamento   #Dosis
   ayunas             <0.44                hipoglusemia            2               4
   ayunas          [0.44 - 0.61)             normal             Ninguno            0
   ayunas          [0.61 - 0.7)              elevado               1               6
   ayunas            >=0.7                  diabetes               1               12
 posprandial          <0.78                  normal             Ninguno            0
 posprandial       [0.78 - 1.1)              elevado               1               9
 posprandial         >=1.1                  diabetes               1               18

Si no se encuentra la categoría (valor distinto de “ayunas” y “posprandial” en ayunas)
del paciente el registro cuenta, pero no se entrega ningún tipo de medicamento.
Finalmente, se debe mostrar la cantidad de pacientes atendidos, la cantidad de
pacientes a los que se les hizo entrega del medicamento 1 junto al porcentaje de estos
respecto al total de pacientes atendidos formateado a 2 cifras decimales y la cantidad
de pacientes a los que se les hizo entrega del medicamento 2 junto al porcentaje de
estos respecto al total de pacientes atendidos formateado a 2 cifras decimales.
Además, si no se entregan medicamentos se debe mostrar que el total de pacientes
atendidos, pacientes a los que se les hizo entrega del medicamento 1 y pacientes a los
que se les hizo entrega del medicamento 2 es 0 y sus porcentajes correspondientes son
0.00%.

'''

#Entradas
#Ingrese la cantidad de existencias del medicamento 1
medicamento1 = int(input())
#Ingrese la cantidad de existencias del medicamento 1
medicamento2 = int(input())

#Inicialización de cantidad de pacientes atendidos
pacientes = 0
pacientesMed1 = 0
pacientesMed2 = 0

#Ciclo para controlar la cantidad de pacientes
while medicamento1>0 and medicamento2>0: 
    #Ingrese el estado del paciente (ayunas|posprandial): 
    estado = input()
    #Ingrese el nivel de glucosa en la sangre en mmol/dl: 
    nivelGlucosa = float(input())       
    pacientes += 1
    #Condicionales para establecer parámetros de tabla de rangos
    if estado == 'ayunas':
        if nivelGlucosa<0.44:
            pacientesMed2 += 1
            medicamento2 -= 4            
        elif 0.61<=nivelGlucosa<0.7:
            pacientesMed1 += 1
            medicamento1 -= 6
        elif nivelGlucosa>=0.7:
            pacientesMed1 += 1
            medicamento1 -= 12
    elif estado == 'posprandial':
        if 0.78<=nivelGlucosa<1.1:
            pacientesMed1 += 1
            medicamento1 -= 9
        elif nivelGlucosa>=1.1:
            pacientesMed1 += 1
            medicamento1 -= 18

#Porcentajes de pacientes con medicina tipo 1 y 2
porcentajeMed1 = 100*(pacientesMed1/pacientes) if pacientes!=0 else 0
porcentajeMed2 = 100*(pacientesMed2/pacientes) if pacientes!=0 else 0

#Sálidas
print(pacientes)
print(f'{pacientesMed1} {porcentajeMed1:,.2f}%')
print(f'{pacientesMed2} {porcentajeMed2:,.2f}%')

