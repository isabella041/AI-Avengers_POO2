from SortingStrategy import SortingStrategy
from typing import List, Dict

class HeapSort(SortingStrategy):
    def heapify(self, data: List[Dict], n: int, i: int, column: str):
        """Convierte una lista en un heap válido en la posición dada."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left][column] > data[largest][column]:
            largest = left

        if right < n and data[right][column] > data[largest][column]:
            largest = right

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            self.heapify(data, n, largest, column)

    def sort(self, data: List[Dict], column: str) -> List[Dict]:
        """Ordena la lista de diccionarios usando el algoritmo Heap Sort."""
        if not data:
            return []

        sorted_data = data[:]  # Copia de la lista original
        n = len(sorted_data)

        # Construcción del heap (max heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(sorted_data, n, i, column)

        # Extracción de elementos del heap
        for i in range(n - 1, 0, -1):
            sorted_data[i], sorted_data[0] = sorted_data[0], sorted_data[i]
            self.heapify(sorted_data, i, 0, column)

        return sorted_data
