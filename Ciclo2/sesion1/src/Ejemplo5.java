import java.util.Scanner;
public class Ejemplo5 {
    public static void main(String[] args) throws Exception {
        int dia;
        double subtotal,total;
        Scanner Leer = new Scanner(System.in);
        System.out.print("Día: ");
        dia = Leer.nextInt();
        System.out.print("Total a pagar sin descuento: ");
        subtotal = Leer.nextDouble();
        switch (dia){
            case 1:
                total = subtotal*0.95;
                System.out.print("Total a pagar: "+total);
                break;
            case 2:
                total = subtotal*0.97;
                System.out.print("Total a pagar: "+total);
                break;            
            case 3:
                total = subtotal*0.90;
                System.out.print("Total a pagar: "+total);
                break; 
            case 4:
                total = subtotal*0.96;
                System.out.print("Total a pagar: "+total);
                break; 
            case 5:
                total = subtotal*0.94;
                System.out.print("Total a pagar: "+total);
                break;
            case 6:
                total = subtotal*0.98;
                System.out.print("Total a pagar: "+total);
                break;
            case 7:
                total = subtotal*0.99;
                System.out.print("Total a pagar: "+total);
                break;
            default:
                System.out.print("Día invalido");
                break;
        }
        Leer.close();
    }
}