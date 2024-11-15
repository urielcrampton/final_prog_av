package com.ecommerce.tasks;

import com.ecommerce.model.Pedido;
import com.ecommerce.executor.ConsoleColors;

public class EnvioTask implements Runnable {
    private final Pedido pedido;

    public EnvioTask(Pedido pedido) {
        this.pedido = pedido;
    }

    @Override
    public void run() {
        synchronized (pedido) {
            try {
                // Simular el envío
                System.out.println(ConsoleColors.PURPLE + "Enviando pedido: " + pedido.getId() + ConsoleColors.RESET);
                Thread.sleep(200); // Simulación de envío
                pedido.setEnviado(true);
                System.out.println(ConsoleColors.GREEN + "Pedido enviado: " + pedido.getId() + ConsoleColors.RESET);

            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}
