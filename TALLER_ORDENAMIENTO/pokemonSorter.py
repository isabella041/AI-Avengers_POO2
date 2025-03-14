from SortingStrategy import SortingStrategy
from typing import List, Dict

class PokemonSorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def setStrategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort(self, data: List[Dict], column: str) -> List[Dict]:
        # Extraer los valores de la columna a ordenar
        column_data = [pokemon[column] for pokemon in data]
        
        # Ordenar usando la estrategia (BubbleSort)
        sorted_column = self._strategy.sort(column_data)

        # Ordenar la lista original basada en los valores ordenados
        return sorted(data, key=lambda x: x[column])