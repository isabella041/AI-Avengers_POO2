from SortingStrategy import SortingStrategy
from typing import List, Dict

class BubbleSort(SortingStrategy):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        n = len(data)
        sorted_data = data.copy()  

        for i in range(n - 1):
            for j in range(n - 1 - i):
                if (not reverse and sorted_data[j][key] > sorted_data[j + 1][key]) or \
                   (reverse and sorted_data[j][key] < sorted_data[j + 1][key]):
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]

        return sorted_data  
