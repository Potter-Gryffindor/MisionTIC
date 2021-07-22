import java.util.Scanner;
public class reto1 {
    public static void main(String[] args) throws Exception {

        Scanner Leer = new Scanner(System.in);
        int numEntradas, numExcelentes = 0;
        String Entrada[] = new String[4];
        numEntradas = Integer.parseInt(Leer.nextLine());        
        double Entradas[][] = new double[numEntradas][4];
        double sumPromTotal = 0, promTotal, promExcelente;
        double sumPromMas = 0, sumPromFem = 0, maxChemical = 0;
        String best="";
        for (int i = 0; i < numEntradas; i++){
            Entrada = Leer.nextLine().split(" ");
            for (int j = 0; j < 4; j++){
                Entradas[i][j] = Double.parseDouble(Entrada[j]);
                if (j == 3){
                    sumPromTotal += Entradas[i][j]; 
                    if (Entradas[i][j]>4.5 && Entradas[i][j]<=5)
                        numExcelentes++;                    
                }
                
            }
            if (Entradas[i][1] == 0)
                sumPromMas += Entradas[i][3];
            else if (Entradas[i][1] == 1)
                sumPromFem += Entradas[i][3];
            
            if (Entradas[i][2] == 1)
                if (Entradas[i][3] > maxChemical || i == 0)
                    switch ((int)Entradas[i][0]){
                        case 1:
                            best = "armando";
                            maxChemical = Entradas[i][3];
                            break;
                        case 2:
                            best = "nicolas";
                            maxChemical = Entradas[i][3];
                            break; 
                        case 3:
                            best = "daniel";
                            maxChemical = Entradas[i][3];
                            break;
                        case 4:
                            best = "maria";
                            maxChemical = Entradas[i][3];
                            break; 
                        case 5:
                            best = "marcela";
                            maxChemical = Entradas[i][3];
                            break;  
                        case 6:
                            best = "alexandra";
                            maxChemical = Entradas[i][3];
                            break;
                    }
                            
        }
        Leer.close(); 
        
        promTotal = sumPromTotal/numEntradas;
        promExcelente = numExcelentes*1.0/numEntradas;  
        System.out.printf("%.2f%n",promTotal);  //Salida 1
        System.out.printf("%.2f%n",promExcelente);  //Salida 2
        //Salida 3
        if (sumPromMas>=sumPromFem)
            System.out.println('m');
        else
            System.out.println('f');
        System.out.print(best); //Salida 4
    }
}
