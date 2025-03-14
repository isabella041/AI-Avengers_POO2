from SortingStrategy import SortingStrategy
from typing import List, Dict

class QuickSort(SortingStrategy):
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
        else:
            pivot = self._data[0][key]
            left = [x for x in self._data[1:] if x[key] <= pivot]
            right = [x for x in self._data[1:] if x[key] > pivot]
            return QuickSort().sort(key).sort(left) + [self._data[0]] + QuickSort().sort(key).sort(right)
