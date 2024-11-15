import java.io.FileWriter;
import java.io.IOException;
import java.lang.management.ManagementFactory;
import java.lang.management.OperatingSystemMXBean;
import java.util.ArrayList;
import java.util.List;

import com.ecommerce.executor.PedidoPrioridadExecutor;
import com.ecommerce.model.Pedido;

public class Main {
    public static void main(String[] args) {
        // Configuraciones de pool de hilos para probar utilizaria la 10 10 20
        int[][] poolSizes = {{5, 5, 5}, {5, 10, 5}, {10, 10, 10}, {20, 10, 10}, {10, 20, 10}, {10, 10, 20}, {10, 15, 20}, {15, 15, 15}, {20, 20, 20}, {20, 30, 40}, {50, 50, 50}, {200, 200, 200}};

        // Crear pedidos (algunos urgentes y otros normales)
        List<Pedido> pedidos = new ArrayList<>();
        for (int i = 1; i <= 200; i++) {
            boolean esUrgente = (i % 5 == 0); // Cada quinto pedido es urgente
            pedidos.add(new Pedido("P" + i, esUrgente));
        }

        // Listas para almacenar los resultados de las pruebas
        List<Integer> poolSizePagoResults = new ArrayList<>();
        List<Integer> poolSizeEmpaquetadoResults = new ArrayList<>();
        List<Integer> poolSizeEnvioResults = new ArrayList<>();
        List<Long> executionTimes = new ArrayList<>();
        List<Long> initialMemory = new ArrayList<>();
        List<Long> finalMemory = new ArrayList<>();
        List<Double> initialCpu = new ArrayList<>();
        List<Double> finalCpu = new ArrayList<>();

        // Estadísticas por etapa
        List<Long> totalTiempoPago = new ArrayList<>();
        List<Long> totalTiempoEmpaquetado = new ArrayList<>();
        List<Long> totalTiempoEnvio = new ArrayList<>();
        
        List<Long> promedioPago = new ArrayList<>();
        List<Long> promedioEmpaquetado = new ArrayList<>();
        List<Long> promedioEnvio = new ArrayList<>();
        
        List<Long> medianaPago = new ArrayList<>();
        List<Long> medianaEmpaquetado = new ArrayList<>();
        List<Long> medianaEnvio = new ArrayList<>();
        
        List<Long> minimoPago = new ArrayList<>();
        List<Long> minimoEmpaquetado = new ArrayList<>();
        List<Long> minimoEnvio = new ArrayList<>();

        List<Long> maximoPago = new ArrayList<>();
        List<Long> maximoEmpaquetado = new ArrayList<>();
        List<Long> maximoEnvio = new ArrayList<>();

        // Crear el bean de sistema para obtener la información del sistema
        OperatingSystemMXBean osBean = ManagementFactory.getOperatingSystemMXBean();

        // Ejecutar pruebas con diferentes configuraciones de pool sizes
        for (int[] sizes : poolSizes) {
            System.out.println("========== Ejecución con poolSize: " + sizes[0] + ", " + sizes[1] + ", " + sizes[2] + " ==========");

            // Monitoreo del uso de CPU y memoria antes de la ejecución
            long memoriaInicial = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
            double cpuInicial = osBean.getSystemLoadAverage();

            // Crear el ejecutor de prioridad con tamaños de pool variables
            PedidoPrioridadExecutor pedidoExecutor = new PedidoPrioridadExecutor(sizes[0], sizes[1], sizes[2]);

            // Medir el tiempo de ejecución
            long startTime = System.currentTimeMillis();

            // Añadir todos los pedidos al ejecutor
            for (Pedido pedido : pedidos) {
                pedidoExecutor.agregarPedido(pedido);
            }

            // Procesar los pedidos
            pedidoExecutor.procesarPedidos();

            // Cerrar el ejecutor después de completar las tareas
            pedidoExecutor.shutdown();

            // Medir el tiempo de ejecución total
            long endTime = System.currentTimeMillis();
            long elapsedTime = endTime - startTime;

            // Monitoreo del uso de CPU y memoria después de la ejecución
            long memoriaFinal = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
            double cpuFinal = osBean.getSystemLoadAverage();

            // Almacenar resultados en listas
            poolSizePagoResults.add(sizes[0]);
            poolSizeEmpaquetadoResults.add(sizes[1]);
            poolSizeEnvioResults.add(sizes[2]);
            executionTimes.add(elapsedTime);
            initialMemory.add(memoriaInicial / 1024); // Convertir a KB
            finalMemory.add(memoriaFinal / 1024); // Convertir a KB
            initialCpu.add(cpuInicial); // Usar el promedio de carga del sistema
            finalCpu.add(cpuFinal); // Usar el promedio de carga del sistema

            // Obtener estadísticas de cada etapa
            long[] statsPago = pedidoExecutor.getEstadisticasEtapa("Pago");
            long[] statsEmpaquetado = pedidoExecutor.getEstadisticasEtapa("Empaquetado");
            long[] statsEnvio = pedidoExecutor.getEstadisticasEtapa("Envío");

            totalTiempoPago.add(statsPago[0]);
            promedioPago.add(statsPago[1]);
            medianaPago.add(statsPago[2]);
            minimoPago.add(statsPago[3]);
            maximoPago.add(statsPago[4]);

            totalTiempoEmpaquetado.add(statsEmpaquetado[0]);
            promedioEmpaquetado.add(statsEmpaquetado[1]);
            medianaEmpaquetado.add(statsEmpaquetado[2]);
            minimoEmpaquetado.add(statsEmpaquetado[3]);
            maximoEmpaquetado.add(statsEmpaquetado[4]);

            totalTiempoEnvio.add(statsEnvio[0]);
            promedioEnvio.add(statsEnvio[1]);
            medianaEnvio.add(statsEnvio[2]);
            minimoEnvio.add(statsEnvio[3]);
            maximoEnvio.add(statsEnvio[4]);

            System.out.println("Tiempo de ejecución: " + elapsedTime + " ms");
            System.out.println("Uso de memoria (inicial -> final): " + (memoriaInicial / 1024) + " KB -> " + (memoriaFinal / 1024) + " KB");
            System.out.println("Promedio de CPU (inicial -> final): " + cpuInicial + " -> " + cpuFinal);
            System.out.println("Estadísticas de tiempo por etapa:");
            System.out.println();
            pedidoExecutor.mostrarEstadisticas();

            System.out.println("\n===========================================\n");
        }

        // Formar el CSV con los resultados obtenidos
        try (FileWriter csvWriter = new FileWriter("resultados_pedidos.csv")) {
            csvWriter.append("PoolSizePago,PoolSizeEmpaquetado,PoolSizeEnvio,Tiempo Ejecución (ms),Memoria Inicial (KB),Memoria Final (KB),CPU Inicial,CPU Final,Tiempo TotalPago,Tiempo PromedioPago,Tiempo MedianoPago,Tiempo MínimoPago,Tiempo MáximoPago,Tiempo TotalEmpaquetado,Tiempo PromedioEmpaquetado,Tiempo MedianoEmpaquetado,Tiempo MínimoEmpaquetado,Tiempo MáximoEmpaquetado,Tiempo TotalEnvio,Tiempo PromedioEnvio,Tiempo MedianoEnvio,Tiempo MínimoEnvio,Tiempo MáximoEnvio\n");
            
            for (int i = 0; i < poolSizePagoResults.size(); i++) {
                csvWriter.append(String.format("%d,%d,%d,%d,%d,%d,%.2f,%.2f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n",
                        poolSizePagoResults.get(i),
                        poolSizeEmpaquetadoResults.get(i),
                        poolSizeEnvioResults.get(i),
                        executionTimes.get(i),
                        initialMemory.get(i),
                        finalMemory.get(i),
                        initialCpu.get(i),
                        finalCpu.get(i),
                        totalTiempoPago.get(i),
                        promedioPago.get(i),
                        medianaPago.get(i),
                        minimoPago.get(i),
                        maximoPago.get(i),
                        totalTiempoEmpaquetado.get(i),
                        promedioEmpaquetado.get(i),
                        medianaEmpaquetado.get(i),
                        minimoEmpaquetado.get(i),
                        maximoEmpaquetado.get(i),
                        totalTiempoEnvio.get(i),
                        promedioEnvio.get(i),
                        medianaEnvio.get(i),
                        minimoEnvio.get(i),
                        maximoEnvio.get(i)));
            }
            System.out.println("Resultados guardados en resultados_pedidos.csv");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
