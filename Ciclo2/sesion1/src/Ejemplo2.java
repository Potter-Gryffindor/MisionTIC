import java.util.Scanner;
public class Ejemplo2 {
    public static void main(String[] args) throws Exception {
        int cantBodega = 0,cantMinima = 0;
        Scanner Leer = new Scanner(System.in);
        System.out.print("Cantidad en bodega: ");
        cantBodega = Leer.nextInt();
        System.out.print("Cantidad mínima requerida: ");
        cantMinima = Leer.nextInt();
        Leer.close();
        if (cantMinima>cantBodega){
            System.out.println("Es necesario realizar el pedido al proveedor.");
        }
        else{
            System.out.println("No es necesario realizar el pedido al proveedor.");
        }
        
    }
}
