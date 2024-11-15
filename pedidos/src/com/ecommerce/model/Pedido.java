package com.ecommerce.model;

public class Pedido implements Comparable<Pedido> {
    private String id;
    private boolean urgente;
    private boolean pagado;
    private boolean empaquetado;
    private boolean enviado;

    public Pedido(String id, boolean urgente) {
        this.id = id;
        this.urgente = urgente;
        this.pagado = false;
        this.empaquetado = false;
        this.enviado = false;
    }

    // Getters y setters
    public String getId() {
        return id;
    }

    public boolean isUrgente() {
        return urgente;
    }

    public boolean isPagado() {
        return pagado;
    }

    public void setPagado(boolean pagado) {
        this.pagado = pagado;
    }

    public boolean isEmpaquetado() {
        return empaquetado;
    }

    public void setEmpaquetado(boolean empaquetado) {
        this.empaquetado = empaquetado;
    }

    public boolean isEnviado() {
        return enviado;
    }

    public void setEnviado(boolean enviado) {
        this.enviado = enviado;
    }

    @Override
    public int compareTo(Pedido otroPedido) {
        // Primero, ordenar por urgencia (true antes que false)
        if (this.urgente && !otroPedido.urgente) {
            return -1; // Este pedido es urgente, tiene mayor prioridad
        } else if (!this.urgente && otroPedido.urgente) {
            return 1; // Este pedido no es urgente, tiene menor prioridad
        } else {
            // Si ambos son iguales en urgencia, ordenar por ID numéricamente
            int thisIdNum = Integer.parseInt(this.id.substring(1)); // Extraer el número del ID
            int otroIdNum = Integer.parseInt(otroPedido.id.substring(1)); // Extraer el número del ID
            
            return Integer.compare(thisIdNum, otroIdNum); // Comparar numéricamente
        }
    }
    
    
}
