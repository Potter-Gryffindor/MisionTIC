'''

RETO 1 (MISIÓNTIC 2022)
Nombre del reto: Detección Temprana de Enfermedades no Transmisible de un
Paciente
Autor: Javier Bayter

Descripción del reto:
En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para
erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos como
parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es el de
salud y bienestar y una de sus metas busca reducir en un tercio la mortalidad prematura
por enfermedades no transmisibles mediante la prevención y el tratamiento.
Debido a esto, el ministerio de salud desea que usted construya un sistema para la
detección temprana de una enfermedad en específico, siendo esta la diabetes, en pos
del mejoramiento de la calidad de vida de los ciudadanos.
Para ello, el sistema debe recibir como entrada los datos una cadena de caracteres
“ayunas” o “posprandial” que determina si el paciente se encuentra o no en ayunas,
seguido de un número real que representa el nivel de glucosa en sangre en mmol/dl y
muestre por pantalla si la persona tiene, está en riesgo o no tiene diabetes.

Tabla de Rangos:
   Estado    Glucosa en Sangre(mmol/dl)   Categoría
   ayunas             <0.44              hipoglusemia
   ayunas          [0.44 - 0.61)           normal
   ayunas          [0.61 - 0.7)            elevado
   ayunas            >=0.7                diabetes
 posprandial          <0.78                normal
 posprandial       [0.78 - 1.1)            elevado
 posprandial         >=1.1                diabetes

Además, para cualquier valor distinto de “ayunas” y “posprandial” en ayunas mostrar el
mensaje “error en los datos”.
'''

#Entradas
#Ingrese el estado del paciente (ayunas|posprandial): 
estado = input()
#Ingrese el nivel de glucosa en la sangre en mmol/dl: 
nivelGlucosa = float(input())

#Condicionales para establecer parámetros de tabla de rangos
if estado == 'ayunas':
    if nivelGlucosa<0.44:
        categoria = 'hipoglusemia'
    elif 0.44<=nivelGlucosa<0.61:
        categoria = 'normal'
    elif 0.61<=nivelGlucosa<0.7:
        categoria = 'elevado'
    elif nivelGlucosa>=0.7:
        categoria = 'diabetes'
elif estado == 'posprandial':
    if nivelGlucosa<0.78:
        categoria = 'normal'
    elif 0.78<=nivelGlucosa<1.1:
        categoria = 'elevado'
    elif nivelGlucosa>=1.1:
        categoria = 'diabetes'
else:
    categoria = 'error en los datos'

#Sálida
print(categoria)
    