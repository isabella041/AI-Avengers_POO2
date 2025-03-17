from SortingStrategy import SortingStrategy
from typing import List, Dict

class BubbleSort(SortingStrategy):
    def sort(self, data: List[Dict], key: str) -> List[Dict]:
        """Ordena la lista usando Bubble Sort según la clave proporcionada."""
        n = len(data)
        sorted_data = data.copy()  # Evita modificar la lista original

        for i in range(n - 1):
            for j in range(n - 1 - i):
                if sorted_data[j][key] > sorted_data[j + 1][key]:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]

        return sorted_data
