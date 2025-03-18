from SortingStrategy import SortingStrategy
from typing import List, Dict

class MergeSort(SortingStrategy):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        """Ordena la lista usando Merge Sort según la clave proporcionada."""
        if len(data) <= 1:
            return data

        # Verificar que la clave exista en todos los elementos
        if any(key not in item for item in data):
            raise KeyError(f"La clave '{key}' no existe en los datos.")

        mid = len(data) // 2
        left = self.sort(data[:mid], key, reverse)
        right = self.sort(data[mid:], key, reverse)

        return self._merge(left, right, key, reverse)

    def _merge(self, left: List[Dict], right: List[Dict], key: str, reverse: bool) -> List[Dict]:
        """Función auxiliar para combinar dos listas ordenadas."""
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if (left[i][key] <= right[j][key]) != reverse:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
