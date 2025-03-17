from SortingStrategy import SortingStrategy
from typing import List, Dict

class BucketSort(SortingStrategy):
    def sort(self, data: List[Dict], column: str) -> List[Dict]:
        if not data:
            return []

        max_val = max(data, key=lambda x: x[column])[column]
        min_val = min(data, key=lambda x: x[column])[column]
        bucket_count = len(data)
        buckets = [[] for _ in range(bucket_count)]

        for item in data:
            index = int((item[column] - min_val) / (max_val - min_val + 1) * (bucket_count - 1))
            buckets[index].append(item)

        for bucket in buckets:
            bucket.sort(key=lambda x: x[column])

        return [item for bucket in buckets for item in bucket]
