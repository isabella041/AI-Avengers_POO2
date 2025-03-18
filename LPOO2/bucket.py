from SortingStrategy import SortingStrategy
from typing import List, Dict

class BucketSort(SortingStrategy):
    def sort(self, data: List[Dict], column: str, reverse: bool = False) -> List[Dict]:
        if not data:
            return []

        # Encontrar el valor máximo y mínimo en la columna
        max_val = max(data, key=lambda x: x[column])[column]
        min_val = min(data, key=lambda x: x[column])[column]
        bucket_count = len(data)

        # Crear los buckets vacíos
        buckets = [[] for _ in range(bucket_count)]

        # Distribuir los datos en los buckets
        for item in data:
            index = int((item[column] - min_val) / (max_val - min_val + 1) * (bucket_count - 1))
            buckets[index].append(item)

        # Ordenar cada bucket
        for bucket in buckets:
            bucket.sort(key=lambda x: x[column], reverse=reverse)

        # Concatenar los buckets
        sorted_data = [item for bucket in buckets for item in bucket]

        # Si es orden descendente, invertir el resultado
        return sorted_data if not reverse else sorted_data[::-1]
