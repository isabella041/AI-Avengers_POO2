from SortingStrategy import SortingStrategy
from typing import List, Dict

class SelectionSort(SortingStrategy):
    def sort(self, data: List[Dict], column: str) -> List[Dict]:
        """Ordena la lista de diccionarios usando el algoritmo Selection Sort."""
        if not data:
            return []  # Retorna lista vacía si no hay datos

        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if column not in data[j] or column not in data[min_idx]:
                    raise KeyError(f"La columna '{column}' no existe en los datos.")
                if data[j][column] < data[min_idx][column]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]

        return data
