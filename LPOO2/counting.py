from SortingStrategy import SortingStrategy
from typing import List, Dict

class CountingSort(SortingStrategy):
    def sort(self, data: List[Dict], column: str) -> List[Dict]:
        if not data:
            return []
        
        # Verificar si la columna contiene datos numéricos
        try:
            for item in data:
                item[column] = float(item[column])  # Convierte a float o usa int() si son enteros
        except ValueError:
            raise ValueError(f"CountingSort solo puede ordenar valores numéricos. La columna '{column}' contiene datos no numéricos.")
        
        # Encontrar el valor máximo y mínimo en la columna
        max_val = max(data, key=lambda x: x[column])[column]
        min_val = min(data, key=lambda x: x[column])[column]
        range_of_elements = int(max_val - min_val + 1)
        
        # Inicializar listas de conteo y salida
        count = [0] * range_of_elements
        output = [None] * len(data)
        
        # Contar la frecuencia de cada valor
        for item in data:
            count[int(item[column] - min_val)] += 1
        
        # Acumular conteos
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        # Construir salida ordenada
        for item in reversed(data):
            output[count[int(item[column] - min_val)] - 1] = item
            count[int(item[column] - min_val)] -= 1
        
        return output