## Sesión # 2: Componente Práctico

Una determinada empresa tiene tres listas de tamaño N, las cuales corresponden a:
1. El código del producto
2. La cantidad en bodega del producto.
3. La cantidad mínima requerida del producto.

Para el sistema de inventario es importante conocer si es necesario solicitar un determinado
producto a su proveedor de acuerdo a la cantidad mínima requerida. Se requiere un algoritmo
que:
- Lea el número de productos.
- Lea las 3 listas y almacene cada lista en un vector.

Una vez leídos los datos:
- Indique los códigos de los productos de los cuales se deben realizar los pedidos.
- Indique el código del producto con mayor y menor número de unidades en bodega.

**Ejemplos:**

Tamaño de las listas: 7

Lista de códigos
| 354 | 256 | 127 | 390 | 35 | 562 | 236 |
|-----|-----|-----|-----|----|-----|-----|

Lista de cantidad en bodega
| 10  | 150 | 56  | 24  | 36 | 90  | 15  |
|-----|-----|-----|-----|----|-----|-----|

Lista de cantidad mínima requerida
| 17  | 34  | 60  | 56  | 32 | 16  | 5   |
|-----|-----|-----|-----|----|-----|-----|

``` 
Códigos de productos que son necesario pedir:
354
127
390
Código con mayor número unidades: 256
Código con menor número unidades: 354
```
