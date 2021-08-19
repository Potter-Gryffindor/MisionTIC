public class App {
    public static void main(String[] args) throws Exception {
        //Instanciamiento del objeto
        SchoolGradingSystem claseF = new SchoolGradingSystem();
        
        //Entrada
        claseF.readData();
        
        //Salida
        System.out.printf("%.2f%n",claseF.question1());
        System.out.printf("%.2f%n",claseF.question2());
        System.out.printf("%s%n",claseF.question3());
        System.out.printf("%s%n",claseF.question4());            
    }
}
