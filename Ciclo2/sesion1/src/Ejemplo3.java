import java.util.Scanner;
public class Ejemplo3 {
    public static void main(String[] args) throws Exception {
        int cantBodega = 0,cantMinima = 0, diferencia = 0;
        Scanner Leer = new Scanner(System.in);
        System.out.print("Cantidad en bodega: ");
        cantBodega = Leer.nextInt();
        System.out.print("Cantidad mínima requerida: ");
        cantMinima = Leer.nextInt();
        Leer.close();
        diferencia = cantBodega-cantMinima;        
        if (cantMinima>cantBodega){
            System.out.println("Es necesario realizar el pedido al proveedor.");
        }
        else if (diferencia<10){
            System.out.println("No es necesario realizar el pedido al proveedor. Unidades que hacen falta vender: "+(diferencia)+". Alerta generada.");    
        }
        else {
            System.out.println("No es necesario realizar el pedido al proveedor. Unidades que hacen falta vender: "+(diferencia)+".");
        }
    }
}
