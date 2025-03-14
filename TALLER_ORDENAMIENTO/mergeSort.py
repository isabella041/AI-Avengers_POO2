from SortingStrategy import SortingStrategy
from typing import List, Dict

class MergeSort(SortingStrategy):
    def __init__(self):
        self._data = []

    # Setter
    def setData(self, newData: List[Dict]) -> None:
        self._data = newData

    # Getter
    def getData(self) -> List[Dict]:
        return self._data

    # Método de ordenamiento
    def sort(self, key: str) -> List[Dict]:
        if len(self._data) <= 1:
            return self._data

        mid = len(self._data) // 2
        left_half = MergeSort()
        right_half = MergeSort()

        # Dividir los datos
        left_half.setData(self._data[:mid])
        right_half.setData(self._data[mid:])

        # Ordenar cada mitad recursivamente
        left_sorted = left_half.sort(key)
        right_sorted = right_half.sort(key)

        # Combinar las dos mitades ordenadas
        return self._merge(left_sorted, right_sorted, key)

    def _merge(self, left: List[Dict], right: List[Dict], key: str) -> List[Dict]:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][key] <= right[j][key]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Añadir elementos restantes
        result.extend(left[i:])
        result.extend(right[j:])

        return result
