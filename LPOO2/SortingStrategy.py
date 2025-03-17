from typing import List, Dict
from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[Dict], key: str) -> List[Dict]:
        """Método abstracto que cada estrategia de ordenamiento debe implementar."""
        pass
