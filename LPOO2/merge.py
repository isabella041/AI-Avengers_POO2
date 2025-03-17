from SortingStrategy import SortingStrategy
from typing import List, Dict

class MergeSort(SortingStrategy):
    def sort(self, data: List[Dict], key: str) -> List[Dict]:
        """Ordena la lista usando Merge Sort según la clave proporcionada."""
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left = self.sort(data[:mid], key)
        right = self.sort(data[mid:], key)

        return self._merge(left, right, key)

    def _merge(self, left: List[Dict], right: List[Dict], key: str) -> List[Dict]:
        """Función auxiliar para combinar dos listas ordenadas."""
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][key] <= right[j][key]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
