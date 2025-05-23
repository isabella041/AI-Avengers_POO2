from SortingStrategy import SortingStrategy
from typing import List, Dict

class PokemonSorter:
    def __init__(self, strategy: SortingStrategy):
        """Inicializa el sorter con una estrategia de ordenamiento."""
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        """Cambia la estrategia de ordenamiento en tiempo de ejecución."""
        if not isinstance(strategy, SortingStrategy):
            raise TypeError("La estrategia debe ser una instancia de SortingStrategy")
        self._strategy = strategy

    def sort(self, data: List[Dict], column: str, reverse: bool = False) -> List[Dict]:
        """Ordena los datos según la estrategia seleccionada.
        
        Parámetros:
        - data: Lista de diccionarios con los datos de los Pokémon.
        - column: Nombre de la columna por la que se quiere ordenar.
        - reverse: Si es `True`, ordena de mayor a menor.
        
        Retorna:
        - Lista ordenada de diccionarios.
        """
        if not data:
            return []  # Retorna lista vacía si no hay datos
        
        if column not in data[0]:
            raise KeyError(f"La columna '{column}' no existe en los datos.")

        return self._strategy.sort(data, column, reverse)
