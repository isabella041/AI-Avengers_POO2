from SortingStrategy import SortingStrategy
from typing import List, Dict

class HeapSort(SortingStrategy):
    def heapify(self, data: List[Dict], n: int, i: int, column: str, reverse: bool):
        """Convierte una lista en un heap válido en la posición dada."""
        extreme = i  # Puede ser el máximo o el mínimo
        left = 2 * i + 1
        right = 2 * i + 2

        # Comparación flexible según el orden requerido
        if left < n and ((data[left][column] > data[extreme][column]) != reverse):
            extreme = left

        if right < n and ((data[right][column] > data[extreme][column]) != reverse):
            extreme = right

        # Si el extremo cambia, intercambiar y seguir ajustando el heap
        if extreme != i:
            data[i], data[extreme] = data[extreme], data[i]
            self.heapify(data, n, extreme, column, reverse)

    def sort(self, data: List[Dict], column: str, reverse: bool = False) -> List[Dict]:
        """Ordena la lista de diccionarios usando el algoritmo Heap Sort."""
        if not data:
            return []

        sorted_data = data[:]  # Copia de la lista original para no modificarla
        n = len(sorted_data)

        # Construcción del heap (max heap o min heap según `reverse`)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(sorted_data, n, i, column, reverse)

        # Extracción de elementos del heap
        for i in range(n - 1, 0, -1):
            sorted_data[i], sorted_data[0] = sorted_data[0], sorted_data[i]
            self.heapify(sorted_data, i, 0, column, reverse)

        return sorted_data
