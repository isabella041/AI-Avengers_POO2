from SortingStrategy import SortingStrategy
from typing import List, Dict

class InsertionSort(SortingStrategy):
    def sort(self, data: List[Dict], column: str) -> List[Dict]:
        """Ordena la lista de diccionarios usando el algoritmo Insertion Sort."""
        if not data:
            return []

        sorted_data = data[:]  # Copia de la lista original
        n = len(sorted_data)

        for i in range(1, n):
            key_item = sorted_data[i]
            j = i - 1

            while j >= 0:
                if column not in sorted_data[j]:
                    raise KeyError(f"La columna '{column}' no existe en los datos.")

                if key_item[column] < sorted_data[j][column]:
                    sorted_data[j + 1] = sorted_data[j]
                    j -= 1
                else:
                    break

            sorted_data[j + 1] = key_item

        return sorted_data
