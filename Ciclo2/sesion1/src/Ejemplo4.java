import java.util.Scanner;
public class Ejemplo4 {
    public static void main(String[] args) throws Exception {
        int cantBodega = 0, cantMinima = 0, diferencia = 0, cantDeseada = 0;
        float valorCompra = 0, valorCaja = 0, subtotal = 0;
        Scanner Leer = new Scanner(System.in);
        System.out.print("Cantidad en bodega: ");
        cantBodega = Leer.nextInt();
        System.out.print("Cantidad mínima requerida: ");
        cantMinima = Leer.nextInt();
        diferencia = cantBodega-cantMinima;        
        if (cantMinima>cantBodega){
            System.out.println("Es necesario realizar el pedido al proveedor.");
            System.out.print("Cantidades de compra deseada: ");
            cantDeseada = Leer.nextInt();
            System.out.print("Valor de compra: ");
            valorCompra = Leer.nextFloat();
            System.out.print("Valor en caja: ");
            valorCaja = Leer.nextFloat();
            subtotal = valorCompra*cantDeseada;
            if (subtotal<valorCaja){
                System.out.println("Si es posible realizar el pedido.");
            }
            else{
                System.out.println("No es posible realizar el pedido.");
            }
        }
        else if (diferencia<10){
            System.out.println("No es necesario realizar el pedido al proveedor. Unidades que hacen falta vender: "+(diferencia)+". Alerta generada.");    
        }
        else {
            System.out.println("No es necesario realizar el pedido al proveedor. Unidades que hacen falta vender: "+(diferencia)+".");
        }
        Leer.close();
    }
}