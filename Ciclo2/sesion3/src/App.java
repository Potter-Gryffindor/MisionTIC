import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        Scanner Leer = new Scanner(System.in);
        int productos = 0, sedes = 0; 
        double sum;

        String Entrada1 = Leer.nextLine();
        String Entrada2 = Leer.nextLine();
        String Entrada3 = Leer.nextLine();

        String strCodes[] = Entrada1.split(" ");
        String strBodega[] = Entrada2.split(";"); 
        String strMinReq[] = Entrada3.split(";"); 
        
        productos = strCodes.length;
        sedes = strBodega.length;

        int codigos[] =  new int[productos];
        int bodegas[][] = new int[sedes][productos];
        int minRequerido[][] = new int[sedes][productos];
        double promedio[] = new double[productos];

        String bodegasAux[] = new String[productos];
        String minRequeridoAux[] = new String[productos];

        for (int j = 0; j < sedes; j++){
            bodegasAux = strBodega[j].split(" ");
            minRequeridoAux = strMinReq[j].split(" ");
            for (int i = 0; i < productos; i++){
                if (j==0){
                    codigos[i] = Integer.parseInt(strCodes[i]);
                }
                bodegas[j][i] = Integer.parseInt(bodegasAux[i]);
                minRequerido[j][i] = Integer.parseInt(minRequeridoAux[i]);
                if (minRequerido[j][i]>bodegas[j][i]){
                    System.out.printf("Se debe solicitar producto %d en sede %d%n",codigos[i],j);
                }
            }
        }
        System.out.print("\n");
        for (int i = 0; i < productos; i++){
            sum = 0;
            for (int j = 0; j < sedes; j++){
                sum += bodegas[j][i];
            }
            promedio[i] = sum/sedes;
            System.out.printf("El promedio de productos del codigo %d es %.2f%n",codigos[i],promedio[i]);
        }
        Leer.close();
    }
}
