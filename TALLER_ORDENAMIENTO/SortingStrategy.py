from typing import List, Dict
from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[Dict]) -> List[Dict]:
        pass

