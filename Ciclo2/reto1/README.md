# RETO 1 (MISIÓNTIC 2022)
**Nombre del reto:** Diseño de sistema estadístico para escuela\
**Autor:** Javier Bayter

## Descripción del reto:
Una escuela primaria desea implementar un sistema estadístico de clasificación de
notas de los exámenes de sus estudiantes.

La escuela utiliza un sistema de notas basado en números que van desde el 0 hasta el
5, con diferentes rangos con labels que enfatizan el desempeño de los estudiantes.

El sistema debe generar datos estadísticos que puedan ayudar a los profesores a
identificar grupos o estudiantes con dificultades. Actualmente se cuenta con la
información de las calificaciones de los exámenes para cada uno de los estudiantes de
la clase F, el sistema debe generar los datos estadísticos a partir de los siguiente
información:


| Nombre    | Género |   Materia   | Nota |
|:---------:|:------:|:-----------:|:----:|
| alexandra |   f    | matematicas | 3.9  |
|  daniel   |   m    | matematicas | 5.0  |
| alexandra |   f    |   idiomas   | 3.8  |
|  daniel   |   m    |   idiomas   | 2.9  |


Las calificaciones en la escuela se asignan con la siguiente escala de rangos:

| Rango de notas| Calificación  | 
|:-------------:|:-------------:|
|  (4.5 - 5.0]  |  Excelente    |
|  (3.5 - 4.5]  | Sobresaliente |
|  (2.5 - 3.5]  |   Regular     |
|  (1.0 - 2.5]  | Insuficiente  |
|  (0.0 - 1.0]  |  Deficiente   |

                
        
El algoritmo debe ser capaz de responder a las siguientes preguntas:
- ¿Cuál es el desempeño promedio de todo el grupo?
- ¿Qué porcentaje de los exámenes fueron Excelentes?
- ¿Qué género tiene un mejor desempeño promedio?
- ¿Cuál es el estudiante con el mejor desempeño para la materia química?
        
### EJEMPLO

Para facilitar el proceso de ingreso y manipulación de los datos, los valores de tipo
string se les asignará un identificador numérico único por categorías:

| Nombre        | Identificador  | 
|:-------------:|:--------------:|
|  armando      |       1        |
|  nicolas      |       2        |
|  daniel       |       3        |
|  maria        |       4        |
|  marcela      |       5        |
|  alexandra    |       6        |

| Materia        | Identificador  | 
|:--------------:|:--------------:|
|  quimica       |       1        |
|  idiomas       |       2        |
|  historia      |       3        |

| Género         | Identificador  | 
|:--------------:|:--------------:|
|  m             |       0        |
|  f             |       1        |

**Entrada del programa**
```
18
1.0 0.0 1.0 1.3
1.0 0.0 2.0 1.6
1.0 0.0 3.0 0.6
2.0 0.0 1.0 4.7
2.0 0.0 2.0 0.1
2.0 0.0 3.0 4.7
3.0 0.0 1.0 1.2
3.0 0.0 2.0 1.4
3.0 0.0 3.0 1.0
4.0 1.0 1.0 0.4
4.0 1.0 2.0 0.8
4.0 1.0 3.0 1.7
5.0 1.0 1.0 0.2
5.0 1.0 2.0 2.6
5.0 1.0 3.0 0.2
6.0 1.0 1.0 0.5
6.0 1.0 2.0 2.1
6.0 1.0 3.0 1.0                   
```
**Salida del programa**
```
1.45
0.11
m
nicolas
```

Otro aspecto importante es el formato de entrada de los datos, la primera línea de la entrada se trata del número de registros que se deben leer. Las líneas de los registros tienen un formato de tabla, el orden de las columnas es: nombre, género, materia y calificación, las columnas están separadas por un espacio. Se recomienda copiar y pegar este ejemplo en la terminal para realizar pruebas.

### Notas: 
- Prestar especial cuidado a las notaciones de los rangos.
- Se considera aprobado a una calificación igual o mayor a Regular.
- Los elementos con un identificador menor tienen prioridad, al ejecutar un proceso y este arroja varios posibles resultados, se debe imprimir el que tenga      menor identificador.
