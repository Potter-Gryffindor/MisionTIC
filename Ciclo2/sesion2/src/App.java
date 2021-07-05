import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        Scanner Leer = new Scanner(System.in);
        int numProduct=0,min = 0,max = 0, idxMax = 0, idxMin = 0;
        System.out.print("Número de productos: ");
        numProduct=Leer.nextInt();
        int listCodes[] = new int[numProduct];
        int listBodega[] = new int[numProduct]; 
        int listMin[] = new int[numProduct];  
        for (int i = 0; i < numProduct; i++) {
            System.out.printf("Producto %d:%n",i+1);
            System.out.print("Código: ");
            listCodes[i] = Leer.nextInt();
            System.out.print("Cantidad en bodega: ");
            listBodega[i] = Leer.nextInt();
            System.out.print("Cantidad mínima requerida: ");
            listMin[i] = Leer.nextInt();
        }
        Leer.close();
        System.out.println("Códigos de productos que son necesario pedir:");
        for (int j = 0; j < numProduct;j++){
            if (listBodega[j]>max || j==0){
                max = listBodega[j];
                idxMax = j;
            }
            if (listBodega[j]<min || j==0){
                min = listBodega[j];
                idxMin = j;
            }
            if (listBodega[j]<listMin[j]){
                System.out.println(listCodes[j]);
            }
        }
        System.out.printf("Código con mayor número unidades: %d%n",listCodes[idxMax]);
        System.out.printf("Código con menor número unidades: %d",listCodes[idxMin]);
    }
}
