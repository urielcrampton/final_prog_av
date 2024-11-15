package com.ecommerce.executor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.*;
import com.ecommerce.model.Pedido;
import com.ecommerce.tasks.EmpaquetadoTask;
import com.ecommerce.tasks.EnvioTask;
import com.ecommerce.tasks.PagoTask;

public class PedidoPrioridadExecutor {
    private final List<Pedido> pedidosQueue; // Cola para todos los pedidos
    private final List<Pedido> pedidosProcesados;
    private List<Long> tiemposPago = new ArrayList<>();
    private List<Long> tiemposEmpaquetado = new ArrayList<>();
    private List<Long> tiemposEnvio = new ArrayList<>();
    private final ExecutorService pagoExecutor;
    private final ExecutorService empaquetadoExecutor;
    private final ExecutorService envioExecutor;

    public PedidoPrioridadExecutor(int pagoPoolSize, int empaquetadoPoolSize, int envioPoolSize) {
        pedidosQueue = new ArrayList<>();
        pedidosProcesados = new ArrayList<>();
        pagoExecutor = Executors.newFixedThreadPool(pagoPoolSize); 
        empaquetadoExecutor = Executors.newFixedThreadPool(empaquetadoPoolSize);
        envioExecutor = Executors.newFixedThreadPool(envioPoolSize);
    }

    public void agregarPedido(Pedido pedido) {
        // Añadir el pedido a la cola en su posición correcta según la prioridad
        int i = 0;
        while (i < pedidosQueue.size() && pedidosQueue.get(i).compareTo(pedido) <= 0) {
            i++;
        }
        pedidosQueue.add(i, pedido); // Insertar el pedido en la posición correcta
    }

    public void procesarPedidos() {
        while (!pedidosQueue.isEmpty()) {
            Pedido pedido = pedidosQueue.remove(0);

            if (pedido != null) {
                // Medir el tiempo de procesamiento de cada etapa
                long startPago = System.currentTimeMillis();
                pagoExecutor.submit(() -> {
                    new PagoTask(pedido).run();
                    long endPago = System.currentTimeMillis();
                    long tiempoPago = endPago - startPago;
                    synchronized (tiemposPago) {
                        tiemposPago.add(tiempoPago);
                    }

                    CountDownLatch latch = new CountDownLatch(1);

                    long startEmpaquetado = System.currentTimeMillis();
                    ForkJoinPool.commonPool().submit(() -> {
                        new EmpaquetadoTask(pedido, latch).run();
                        long endEmpaquetado = System.currentTimeMillis();
                        long tiempoEmpaquetado = endEmpaquetado - startEmpaquetado;
                        synchronized (tiemposEmpaquetado) {
                            tiemposEmpaquetado.add(tiempoEmpaquetado);
                        }
                    });

                    long startEnvio = System.currentTimeMillis();
                    envioExecutor.submit(() -> {
                        try {
                            latch.await(); // Esperar a que termine el empaquetado
                            new EnvioTask(pedido).run();
                            long endEnvio = System.currentTimeMillis();
                            long tiempoEnvio = endEnvio - startEnvio;
                            synchronized (tiemposEnvio) {
                                tiemposEnvio.add(tiempoEnvio);
                            }
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                    });
                });
            }
        }
    }

    public void mostrarEstadisticas() {
        mostrarEstadisticasEtapa("Pago", tiemposPago);
        mostrarEstadisticasEtapa("Empaquetado", tiemposEmpaquetado);
        mostrarEstadisticasEtapa("Envío", tiemposEnvio);
    }

    private void mostrarEstadisticasEtapa(String etapa, List<Long> tiempos) {
        if (tiempos.isEmpty()) {
            System.out.println("No hay datos para " + etapa);
            return;
        }

        Collections.sort(tiempos);
        long total = tiempos.stream().mapToLong(Long::longValue).sum();
        long promedio = total / tiempos.size();
        long mediana = tiempos.size() % 2 == 0 ? 
                       (tiempos.get(tiempos.size() / 2) + tiempos.get((tiempos.size() / 2) - 1)) / 2 : 
                       tiempos.get(tiempos.size() / 2);
        long maximo = tiempos.get(tiempos.size() - 1);
        long minimo = tiempos.get(0);

        System.out.println("Estadísticas de " + etapa + ":");
        System.out.println("Promedio: " + promedio + " ms");
        System.out.println("Mediana: " + mediana + " ms");
        System.out.println("Máximo: " + maximo + " ms");
        System.out.println("Mínimo: " + minimo + " ms");
        System.out.println();
    }
    
    public long[] getEstadisticasEtapa(String etapa) {
        switch (etapa) {
            case "Pago":
                return calcularEstadisticas(tiemposPago);
            case "Empaquetado":
                return calcularEstadisticas(tiemposEmpaquetado);
            case "Envío":
                return calcularEstadisticas(tiemposEnvio);
            default:
                return new long[]{0, 0, 0, 0}; // Para manejar errores
        }
    }

    private long[] calcularEstadisticas(List<Long> tiempos) {
        if (tiempos.isEmpty()) {
            return new long[]{0, 0, 0, 0}; // Retornar ceros si no hay datos
        }

        Collections.sort(tiempos);
        long total = tiempos.stream().mapToLong(Long::longValue).sum();
        long promedio = total / tiempos.size();
        long mediana = tiempos.size() % 2 == 0 ? 
                       (tiempos.get(tiempos.size() / 2) + tiempos.get((tiempos.size() / 2) - 1)) / 2 : 
                       tiempos.get(tiempos.size() / 2);
        long maximo = tiempos.get(tiempos.size() - 1);
        long minimo = tiempos.get(0);

        return new long[]{total, promedio, mediana, minimo, maximo}; // Retornar el total, promedio, mediana, mínimo y máximo
    }



    public void mostrarResumen() {
        System.out.println(ConsoleColors.CYAN + "======= Resumen Final =======");
        System.out.println("+-----------+-----------+-----------+-----------+");
        System.out.printf("| Pedido ID | Pagado    | Empaquetado | Enviado  |\n");
        System.out.println("+-----------+-----------+-----------+-----------+");
        for (Pedido pedido : pedidosProcesados) {
            System.out.printf("| %-9s | %-9s | %-9s | %-9s |\n", 
                pedido.getId(), 
                pedido.isPagado() ? "Sí" : "No", 
                pedido.isEmpaquetado() ? "Sí" : "No", 
                pedido.isEnviado() ? "Sí" : "No");
        }
        System.out.println("+-----------+-----------+-----------+-----------+");
        System.out.println(ConsoleColors.RESET);
    }

    public void shutdown() {
        shutdownExecutor(pagoExecutor);
        shutdownExecutor(empaquetadoExecutor);
        shutdownExecutor(envioExecutor);
    }

    private void shutdownExecutor(ExecutorService executorService) {
        executorService.shutdown();
        try {
            if (!executorService.awaitTermination(60, TimeUnit.SECONDS)) {
                executorService.shutdownNow();
            }
        } catch (InterruptedException e) {
            executorService.shutdownNow();
        }
    }
}
