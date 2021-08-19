import java.util.Scanner;

public class SchoolGradingSystem{
    //Atributos
    private short numEntradas;
    private float[][] datos; 

    //Métodos
    public void readData(){
        Scanner Leer = new Scanner(System.in);
        String[] Entrada;
        numEntradas = Short.parseShort(Leer.nextLine());
        datos = new float[numEntradas][4];
        for (int i = 0; i < numEntradas;i++){
            Entrada = Leer.nextLine().split(" ");
            for (int j = 0; j < 4;j++)
                datos[i][j] = Float.parseFloat(Entrada[j]);                
        }
        Leer.close();
    }
    
    public float question1(){
        float sumNotas=0;
        for (int i = 0; i < numEntradas;i++)
            sumNotas += datos[i][3];
        return sumNotas/numEntradas;
    }

    public float question2(){ 
        short numExcelentes=0;
        for (int i = 0; i < numEntradas; i++)  
            if (datos[i][3]>4.5 && datos[i][3]<=5)
                numExcelentes++;     
        return numExcelentes*1.0f/numEntradas;
    }

    public String question3(){
        float sumMasculino = 0;
        float sumFemenino = 0;
        short numHombres = 0;
        short numMujeres = 0;

        for (int i = 0; i < numEntradas; i++)
            if (datos[i][1] == 0){
                sumMasculino += datos[i][3];
                numHombres++;
            }
            else if (datos[i][1] == 1){
                sumFemenino += datos[i][3];
                numMujeres++;
            }
        if((sumMasculino/numHombres)>=(sumFemenino/numMujeres))
            return "m";
        else
            return "f";
    }

    public String question4(){
        float maxChemical = 0;
        String best="";
        for (int i = 0; i < numEntradas; i++){
            if ((datos[i][2] == 1) && (datos[i][3] > maxChemical || i == 0))
                switch ((int)datos[i][0]){
                    case 1:
                        best = "armando";
                        maxChemical = datos[i][3];
                        break;
                    case 2:
                        best = "nicolas";
                        maxChemical = datos[i][3];
                        break; 
                    case 3:
                        best = "daniel";
                        maxChemical = datos[i][3];
                        break;
                    case 4:
                        best = "maria";
                        maxChemical = datos[i][3];
                        break; 
                    case 5:
                        best = "marcela";
                        maxChemical = datos[i][3];
                        break;  
                    case 6:
                        best = "alexandra";
                        maxChemical = datos[i][3];
                        break;
                    }
        }
        return best;
    }
}