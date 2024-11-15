package com.ecommerce.tasks;

import com.ecommerce.model.Pedido;
import com.ecommerce.executor.ConsoleColors;

public class PagoTask implements Runnable {
    private final Pedido pedido;

    public PagoTask(Pedido pedido) {
        this.pedido = pedido;
    }

    @Override
    public void run() {
        synchronized (pedido) {
            try {
                // Simular el procesamiento del pago
                System.out.println(ConsoleColors.YELLOW + "Procesando pago para el pedido: " + pedido.getId() + ConsoleColors.RESET);
                Thread.sleep(100); // Simulación de tiempo de procesamiento de pago
                pedido.setPagado(true);
                System.out.println(ConsoleColors.ORANGE + "Pago completado para el pedido: " + pedido.getId() + ConsoleColors.RESET);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}
