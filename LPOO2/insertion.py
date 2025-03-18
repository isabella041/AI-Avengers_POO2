from SortingStrategy import SortingStrategy
from typing import List, Dict

class InsertionSort(SortingStrategy):
    def sort(self, data: List[Dict], column: str, reverse: bool = False) -> List[Dict]:
        """Ordena la lista de diccionarios usando el algoritmo Insertion Sort."""
        if not data:
            return []

        # Verificar que la columna exista en todos los elementos
        if any(column not in item for item in data):
            raise KeyError(f"La columna '{column}' no existe en los datos.")

        sorted_data = data[:]  # Copia de la lista original
        n = len(sorted_data)

        for i in range(1, n):
            key_item = sorted_data[i]
            j = i - 1

            # Comparación según el parámetro `reverse`
            while j >= 0 and ((key_item[column] < sorted_data[j][column]) != reverse):
                sorted_data[j + 1] = sorted_data[j]
                j -= 1

            sorted_data[j + 1] = key_item

        return sorted_data
