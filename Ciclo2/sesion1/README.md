## Sesión # 1: Componente Práctico

### Ejemplo 1: Estructura condicional simple

En un sistema de inventario es importante conocer si es necesario solicitar un determinado
producto a su proveedor de acuerdo a una cantidad mínima requerida en bodega. Se requiere
un algoritmo que dada una cantidad en bodega y una cantidad mínima requerida indique si
es necesario o no solicitar el producto al proveedor.

Ejemplos:
* Cantidad en bodega: 500, Cantidad mínima requerida 100. Entonces no es necesario realizar
el pedido al proveedor.
* Cantidad en bodega: 300, Cantidad mínima requerida 450. Entonces si es necesario realizar
el pedido al proveedor.

Requerimiento: utilice sólo condicionales simples.

### Ejemplo 2: Estructura condicional doble

En un sistema de inventario es importante conocer si es necesario solicitar un determinado
producto a su proveedor de acuerdo a una cantidad mínima requerida en bodega. Se requiere
un algoritmo que dada una cantidad en bodega y una cantidad mínima requerida indique si
es necesario o no solicitar el producto al proveedor.

Ejemplos:
* Cantidad en bodega: 500, Cantidad mínima requerida 100. Entonces no es necesario realizar
el pedido al proveedor.
* Cantidad en bodega: 300, Cantidad mínima requerida 450. Entonces si es necesario realizar
el pedido al proveedor.

Requerimiento: utilice condicionales dobles.

### Ejemplo 3: Estructura condicional múltiple.

En un sistema de inventario es importante conocer si es necesario solicitar un determinado
producto a su proveedor de acuerdo a una cantidad mínima requerida en bodega. Se requiere
un algoritmo que dada una cantidad en bodega y una cantidad mínima requerida indique si
es necesario o no solicitar el producto al proveedor. En caso de no ser necesario la solicitud
del producto, indique cuántas unidades hacen falta vender para tener que realizar el pedido
y genere una alerta cuando estas unidas sean menores a 10.

Ejemplos:
* Cantidad en bodega: 500, Cantidad mínima requerida 100. Entonces no es necesario realizar
el pedido al proveedor. Unidades que hacen falta vender: 400.
* Cantidad en bodega: 55, Cantidad mínima requerida 50. Entonces no es necesario realizar
el pedido al proveedor. Unidades que hacen falta vender: 5. Alerta generada.
* Cantidad en bodega: 300, Cantidad mínima requerida 450. Entonces si es necesario realizar
el pedido al proveedor.

Requerimiento: utilice condicionales múltiples.

### Ejemplo 4: Estructura condicional anidado

En un sistema de inventario es importante conocer si es necesario solicitar un determinado
producto a su proveedor de acuerdo a una cantidad mínima requerida en bodega. Se requiere
un algoritmo que dada una cantidad en bodega y una cantidad mínima requerida indique si
es necesario o no solicitar el producto al proveedor.

Adicionalmente, en caso de no ser necesario la solicitud del producto, indique cuántas
unidades hacen falta vender para tener que realizar el pedido y genere una alerta cuando
estas unidades sean menores a 10. Por el contrario si se debe realizar el pedido, debe solicitar
las unidades de compra deseadas, el valor de compra del producto y el dinero en caja con el
fin de validar si es posible realizar la compra.

Ejemplos:
* Cantidad en bodega: 500, Cantidad mínima requerida 100. Entonces no es necesario realizar
el pedido al proveedor. Unidades que hacen falta vender: 400.
* Cantidad en bodega: 55, Cantidad mínima requerida 50. Entonces no es necesario realizar
el pedido al proveedor. Unidades que hacen falta vender: 5. Alerta generada.
* Cantidad en bodega: 300, Cantidad mínima requerida 450. Entonces si es necesario realizar
el pedido al proveedor. Cantidades de compra deseada: 200. Valor de compra: 3350, Valor
en caja: 1.050.000. Si es posible realizar el pedido
* Cantidad en bodega: 300, Cantidad mínima requerida 450. Entonces si es necesario realizar
el pedido al proveedor. Cantidades de compra deseada: 200. Valor de compra: 3350, Valor
en caja: 400.000. No es posible realizar el pedido
Requerimiento: utilice condicionales anidados.

### Ejemplo 5: Estructura dependiendo de o Según

Una determinada empresa ha decidido ofrecer descuentos a sus clientes de acuerdo al día
de la semana en el que se realice la compra, para lo cual se requiere un algoritmo que dado
el día de la semana (en número), y el total a pagar sin descuento, calcule el total incluyendo
el descuento. El descuento se otorga de acuerdo a la siguiente tabla.

| Día | Descuento |
|:----|:----------|
| 1   | 5%        |
| 2   | 3%        |
| 3   | 10%       |
| 4   | 4%        |
| 5   | 6%        |
| 6   | 2%        |
| 7   | 1%        |

### Ejemplo 6: Estructura cíclica

Como parte de un sistema de facturación es necesario conocer el valor unitario y lascantidades a comprar de cada uno de los productos para calcular el total a pagar.

Se requiere un algoritmo que para 1 cliente, calcule el valor a pagar de N tipos de productos
comprados de acuerdo a la cantidad a llevar de cada tipo.

**Ejemplo:**

Cantidad de tipo de productos: 3

Cantidad del producto 1: 4. Valor del producto 1: 2450

Cantidad del producto 2: 10. Valor del producto 2: 6540

Cantidad del producto 3: 1. Valor del producto 3: 1050

Total de la factura: 76250

### Ejemplo 7: Integración estructuras condicionales y cíclicas (while if-else) (for if-else)

Como parte de un sistema de facturación es necesario conocer el valor unitario y las
cantidades a comprar de cada uno de los productos para calcular el total a pagar.

Se requiere un algoritmo que para un conjunto de clientes, calcule para cada uno de ellos el
valor a pagar de N tipos de productos comprados de acuerdo a la cantidad a llevar de cada
tipo. Al finalizar la atención de los clientes, se debe indicar el total vendido por la empresa.
Para las compras superiores a 100.000 la empresa ha decido otorgar un 10% de descuento
sobre el total de la compra.

Nota: Se deben atender a los clientes hasta que el usuario indique lo contrario.

**Ejemplo:**

Cliente 1:

Cantidad de tipo de productos: 3

Cantidad del producto 1: 4. Valor del producto 1: 2450

Cantidad del producto 2: 10. Valor del producto 1: 6540

Cantidad del producto 3: 1. Valor del producto 1: 1050

Total de la factura: 76250



Cliente 2:

Cantidad de tipo de productos: 2

Cantidad del producto 1: 5. Valor del producto 1: 10560

Cantidad del producto 2: 7. Valor del producto 1: 650

Total de la factura: 57350



Total vendido:133600
