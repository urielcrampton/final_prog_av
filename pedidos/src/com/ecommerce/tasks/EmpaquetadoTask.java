package com.ecommerce.tasks;

import com.ecommerce.model.Pedido;
import com.ecommerce.executor.ConsoleColors;

import java.util.concurrent.CountDownLatch;

public class EmpaquetadoTask implements Runnable {
    private final Pedido pedido;
    private final CountDownLatch latch;

    public EmpaquetadoTask(Pedido pedido, CountDownLatch latch) {
        this.pedido = pedido;
        this.latch = latch;
    }

    @Override
    public void run() {
        synchronized (pedido) {
            try {
                // Simular empaquetado
                System.out.println(ConsoleColors.CYAN + "Empaquetando pedido: " + pedido.getId() + ConsoleColors.RESET);
                Thread.sleep(150); // Simulación de empaquetado
                pedido.setEmpaquetado(true);
                System.out.println(ConsoleColors.BLUE + "Pedido empaquetado: " + pedido.getId() + ConsoleColors.RESET);

                latch.countDown(); // Señal de que el empaquetado ha terminado
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}