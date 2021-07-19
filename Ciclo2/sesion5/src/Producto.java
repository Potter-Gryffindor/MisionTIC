public class Producto {
    //Atributos
    private String codigo;
    private float precioCompra;
    private long cantidadBodega;
    private long cantidadMinBodega;    

    //Métodos
    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public float getPrecioCompra() {
        return precioCompra;
    }

    public void setPrecioCompra(float precioCompra) {
        this.precioCompra = precioCompra;
    }

    public long getCantidadBodega() {
        return cantidadBodega;
    }

    public void setCantidadBodega(long cantidadBodega) {
        this.cantidadBodega = cantidadBodega;
    }

    public long getCantidadMinBodega() {
        return cantidadMinBodega;
    }

    public void setCantidadMinBodega(long cantidadMinBodega) {
        this.cantidadMinBodega = cantidadMinBodega;
    }


    public boolean solicitarPedido(){
        return cantidadBodega < cantidadMinBodega;        
    }   
}
