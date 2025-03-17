from SortingStrategy import SortingStrategy
from typing import List, Dict

class QuickSort(SortingStrategy):
    def sort(self, data: List[Dict], key: str) -> List[Dict]:
        """Ordena la lista usando Quick Sort según la clave proporcionada."""
        if len(data) <= 1:
            return data

        pivot = data[0]  # Se toma el primer elemento como pivote
        left = [x for x in data[1:] if x[key] <= pivot[key]]
        right = [x for x in data[1:] if x[key] > pivot[key]]

        return self.sort(left, key) + [pivot] + self.sort(right, key)
