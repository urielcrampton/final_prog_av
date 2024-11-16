from typing import Generic, TypeVar, Callable

# Tipo genérico para el valor dentro de la clase Maybe
T = TypeVar('T')

class Maybe(Generic[T]):
    def __init__(self, value: T = None):
        """
        Inicializa una instancia de la clase Maybe con un valor opcional.

        Args:
            value (T, opcional): El valor a almacenar en la instancia. Por defecto es None.
        """
        self._value = value

    def is_nothing(self) -> bool:
        """
        Verifica si la instancia contiene un valor.

        Returns:
            bool: True si no hay valor (None), False si hay un valor.
        """
        return self._value is None

    def bind(self, func: Callable[[T], 'Maybe']) -> 'Maybe':
        """
        Aplica una función al valor contenido si existe, devolviendo una nueva instancia Maybe.

        Args:
            func (Callable[[T], 'Maybe']): Función que toma un valor de tipo T y devuelve una instancia de Maybe.

        Returns:
            Maybe: Nueva instancia de Maybe resultante de aplicar la función al valor actual,
                   o la misma instancia si no hay valor.
        """
        if self.is_nothing():
            return self
        return func(self._value)

    def get_or_else(self, default: T) -> T:
        """
        Obtiene el valor contenido si existe, de lo contrario devuelve un valor por defecto.

        Args:
            default (T): Valor que se devolverá si no hay valor contenido en la instancia.

        Returns:
            T: El valor contenido si existe, o el valor por defecto si no hay valor.
        """
        return self._value if not self.is_nothing() else default
