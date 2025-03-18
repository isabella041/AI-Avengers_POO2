from SortingStrategy import SortingStrategy
from typing import List, Dict

class SelectionSort(SortingStrategy):
    def sort(self, data: List[Dict], column: str, reverse: bool = False) -> List[Dict]:
        """Ordena la lista de diccionarios usando Selection Sort."""
        if not data:
            return []

        # Verificar que la clave existe en todos los elementos
        if any(column not in item for item in data):
            raise KeyError(f"La clave '{column}' no existe en los datos.")

        sorted_data = data[:]  # Copia de la lista original
        n = len(sorted_data)

        for i in range(n):
            swap_idx = i
            for j in range(i + 1, n):
                if (sorted_data[j][column] < sorted_data[swap_idx][column]) != reverse:
                    swap_idx = j
            sorted_data[i], sorted_data[swap_idx] = sorted_data[swap_idx], sorted_data[i]

        return sorted_data
