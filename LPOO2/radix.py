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

    def sort(self, data: List[Dict], column: str, reverse: bool = False) -> List[Dict]:
        """Ordena la lista de diccionarios usando Radix Sort."""
        if not data:
            return []

        # Verificar que la clave exista en todos los elementos
        if any(column not in item for item in data):
            raise KeyError(f"La clave '{column}' no existe en los datos.")

        # Separar números negativos y positivos
        negatives = [item for item in data if item[column] < 0]
        positives = [item for item in data if item[column] >= 0]

        # Obtener el valor absoluto máximo
        max_val = max(abs(item[column]) for item in data)

        exp = 1
        while max_val // exp > 0:
            positives = self.counting_sort(positives, exp, column)
            negatives = self.counting_sort(negatives, exp, column)
            exp *= 10

        # Unir negativos (orden inverso) y positivos
        sorted_data = negatives[::-1] + positives

        return sorted_data[::-1] if reverse else sorted_data
