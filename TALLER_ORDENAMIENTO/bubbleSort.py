from SortingStrategy import SortingStrategy
from typing import List, Dict

class BubbleSort(SortingStrategy):
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
        n = len(self._data)
        for item in range(n - 1, 0, -1):
            for i in range(item):
                if self._data[i][key] > self._data[i + 1][key]:
                    self._data[i], self._data[i + 1] = self._data[i + 1], self._data[i]
        return self._data
