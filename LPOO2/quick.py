from SortingStrategy import SortingStrategy
from typing import List, Dict

class QuickSort(SortingStrategy):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        """Ordena la lista usando Quick Sort según la clave proporcionada."""
        if len(data) <= 1:
            return data

        # Verificar que la clave exista en todos los elementos
        if any(key not in item for item in data):
            raise KeyError(f"La clave '{key}' no existe en los datos.")

        pivot = data[0]  # Se toma el primer elemento como pivote
        left = [x for x in data[1:] if (x[key] <= pivot[key]) != reverse]
        right = [x for x in data[1:] if (x[key] > pivot[key]) != reverse]

        return self.sort(left, key, reverse) + [pivot] + self.sort(right, key, reverse)
