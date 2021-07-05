import java.util.Scanner;
public class Ejemplo6 {
    public static void main(String[] args) throws Exception {
        int tipoProduct = 0,cantProduct = 0;
        double total = 0, valor = 0;
        Scanner Leer = new Scanner(System.in);
        System.out.print("Cantidad de tipo de productos: ");
        tipoProduct = Leer.nextInt();
        
        for(int i=1;i<=tipoProduct;i++){
            System.out.print("Cantidad del producto "+i+":");
            cantProduct = Leer.nextInt();
            System.out.print("Valor del producto "+i+":");
            valor = Leer.nextInt();
            total += cantProduct*valor;
        }
        System.out.println("Total de la factura: "+total);
        Leer.close();
    }
}