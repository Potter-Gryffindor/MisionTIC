public class App {
    public static void main(String[] args) throws Exception {
        //Instanciamiento
        Producto producto1 = new Producto();

        producto1.setAtributos();
        
        if (producto1.solicitarPedido())
            producto1.alerta();
    }
}
