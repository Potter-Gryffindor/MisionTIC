import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        int numProductos;
        long minCantBodega;
        String codeMin;
        Scanner Leer = new Scanner(System.in);
        System.out.print("Número de productos a manejar: ");
        numProductos = Integer.parseInt(Leer.nextLine());
                
        //Instanciamiento
        Producto[] productos = new Producto[numProductos];
        
        for (int i = 0; i < numProductos; i++){
            Producto producto = new Producto();
            System.out.print("Código: ");
            producto.setCodigo(Leer.nextLine());
            System.out.print("Precio de compra: ");
            producto.setPrecioCompra(Float.parseFloat(Leer.nextLine()));
            System.out.print("Cantidad en bodega: ");
            producto.setCantidadBodega(Long.parseLong(Leer.nextLine()));
            System.out.print("Cantidad mínima requerida en bodega: ");
            producto.setCantidadMinBodega(Long.parseLong(Leer.nextLine()));
            productos[i] = producto; 
        }           
        Leer.close();

        for (Producto product : productos)
            if (product.solicitarPedido())
            System.out.printf("ALERTA%nSe debe solicitar pedido al proveedor del producto con código: %s%n",product.getCodigo());  
        
        minCantBodega = productos[0].getCantidadBodega();
        codeMin = productos[0].getCodigo();
          
        for (int i = 0; i < numProductos; i++){
            if (minCantBodega > productos[i].getCantidadBodega()){
                minCantBodega = productos[i].getCantidadBodega();
                codeMin = productos[i].getCodigo();
            }
        }
        System.out.printf("El código del producto que tiene menor cantidad de unidades en bodega es: %s",codeMin);
        
    }
}
