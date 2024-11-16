import time
from functools import wraps
from typing import Callable

def timeit(func: Callable) -> Callable:
    """
    Decorador para medir el tiempo de ejecución de una función.

    Args:
        func (Callable): La función a la que se aplicará el decorador.

    Returns:
        Callable: La función decorada que imprime el tiempo de ejecución.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Captura el tiempo antes de ejecutar la función
        result = func(*args, **kwargs)  # Ejecuta la función y guarda el resultado
        end_time = time.time()  # Captura el tiempo después de ejecutar la función
        print(f"Tiempo transcurrido: {end_time - start_time:.2f} segundos")  # Imprime el tiempo de ejecución
        return result  # Retorna el resultado de la función ejecutada
    return wrapper
