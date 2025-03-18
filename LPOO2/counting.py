from SortingStrategy import SortingStrategy
from typing import List, Dict

class CountingSort(SortingStrategy):
    def sort(self, data: List[Dict], column: str) -> List[Dict]:
        if not data:
            return []
        
        # Extraer los valores de la columna sin modificar el diccionario original
        try:
            column_values = [int(item[column]) for item in data]  # Convertir a int sin modificar data
        except ValueError:
            raise ValueError(f"CountingSort solo puede ordenar valores numéricos. La columna '{column}' contiene datos no numéricos.")
        
        # Encontrar el valor máximo y mínimo
        max_val = max(column_values)
        min_val = min(column_values)
        range_of_elements = max_val - min_val + 1
        
        # Inicializar listas de conteo y salida
        count = [0] * range_of_elements
        output = [None] * len(data)
        
        # Contar la frecuencia de cada valor
        for value in column_values:
            count[value - min_val] += 1
        
        # Acumular conteos
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        # Construir la lista ordenada sin modificar los datos originales
        for item in reversed(data):
            index = int(item[column]) - min_val  # Se mantiene como int
            output[count[index] - 1] = item
            count[index] -= 1
        
        return output
