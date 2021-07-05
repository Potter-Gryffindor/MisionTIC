import java.util.Scanner;
public class Ejemplo7 {
    public static void main(String[] args) throws Exception {
        int tipoProduct = 0,cantProduct = 0, clientes = 0;
        double total = 0, valor = 0, totalVendido = 0;
        Scanner Leer = new Scanner(System.in);
        System.out.print("Clientes: ");
        clientes = Leer.nextInt();
        for(int i=1;i<=clientes;i++){
            System.out.println("Cliente "+i+": ");
            System.out.print("Cantidad de tipo de productos: ");
            tipoProduct = Leer.nextInt();
            total = 0;
            for(int j=1;j<=tipoProduct;j++){
                System.out.print("Cantidad del producto "+j+":");
                cantProduct = Leer.nextInt();
                System.out.print("Valor del producto "+j+":");
                valor = Leer.nextInt();
                total += cantProduct*valor;
            }
            totalVendido += total; 
            System.out.println("Total de la factura: "+total);
        }       
        System.out.println("Total vendido: "+totalVendido);
        Leer.close();
    }
}