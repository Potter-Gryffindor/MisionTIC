import java.util.Scanner;
public class Ejemplo7 {
    public static void main(String[] args) throws Exception {
        int tipoProduct = 0,cantProduct = 0, clientes = 0;
        double total = 0, valor = 0, totalVendido = 0;
        char opcion;
        Scanner Leer = new Scanner(System.in);
        do{
            clientes++;
            System.out.println("Cliente "+clientes+": ");
            System.out.print("Cantidad de tipo de productos: ");
            tipoProduct = Integer.parseInt(Leer.nextLine());
            total = 0;
            for(int j=1;j<=tipoProduct;j++){
                System.out.print("Cantidad del producto "+j+": ");
                cantProduct = Integer.parseInt(Leer.nextLine());
                System.out.print("Valor del producto "+j+": ");
                valor = Integer.parseInt(Leer.nextLine());
                total += cantProduct*valor;
            }
            if (total>10e4)
                total *= 0.90; 
            totalVendido += total; 
            System.out.println("Total de la factura: "+total);
            System.out.print("Desea continuar(S/N): ");
            opcion =Leer.nextLine().charAt(0);
        }while(opcion=='S');
        System.out.println("Total vendido: "+totalVendido);
        System.out.println("Clientes atendidos: "+clientes);
        Leer.close();    
    }
}