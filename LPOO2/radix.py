from SortingStrategy import SortingStrategy
from typing import List, Dict

class RadixSort(SortingStrategy):
    def counting_sort(self, data: List[Dict], exp: int, column: str) -> List[Dict]:
        """Ordena los datos por un dígito significativo usando Counting Sort."""
        n = len(data)
        output = [None] * n
        count = [0] * 10  # Base decimal (0-9)

        # Contar ocurrencias de cada dígito
        for item in data:
            index = abs(item[column]) // exp % 10  # Usa valor absoluto para manejar negativos
            count[index] += 1

        # Acumulado de posiciones
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Construcción del array ordenado
        for item in reversed(data):
            index = abs(item[column]) // exp % 10
            output[count[index] - 1] = item
            count[index] -= 1

        return output

    def sort(self, data: List[Dict], column: str) -> List[Dict]:
        """Ordena la lista de diccionarios usando Radix Sort."""
        if not data:
            return []

        sorted_data = data[:]  # Copia de la lista original

        try:
            max_val = max(abs(item[column]) for item in sorted_data)
        except KeyError:
            return sorted_data  # Retorna sin cambios si la clave no existe

        exp = 1
        while max_val // exp > 0:
            sorted_data = self.counting_sort(sorted_data, exp, column)
            exp *= 10

        return sorted_data
