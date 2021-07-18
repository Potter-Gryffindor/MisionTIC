import java.util.Scanner;
public class Producto {
    //Atributos
    private String codigo;
    private float precioCompra;
    private long cantidadBodega;
    private long cantidadMinBodega;

    //Métodos
    public void setAtributos(){
        Scanner Leer = new Scanner(System.in);
        System.out.print("Código: ");
        codigo = Leer.nextLine();
        System.out.print("Precio de compra: ");
        precioCompra = Float.parseFloat(Leer.nextLine());
        System.out.print("Cantidad en bodega: ");
        cantidadBodega = Long.parseLong(Leer.nextLine());        
        System.out.print("Cantidad mínima requerida en bodega: ");
        cantidadMinBodega = Long.parseLong(Leer.nextLine());    
        Leer.close();
    }

    public boolean solicitarPedido(){
        return cantidadBodega < cantidadMinBodega;
    }

    public void alerta(){
        System.out.printf("ALERTA%nSe debe solicitar pedido al proveedor del producto con código: %s ",codigo);
    }
}
