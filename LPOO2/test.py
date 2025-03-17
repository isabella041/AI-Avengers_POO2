from burbuja import BubbleSort
from quick import QuickSort
from merge import MergeSort
from pokemon import PokemonSorter

# Datos de prueba
pokemon_data = [
    {"Nombre": "Pikachu", "Peso": 6, "Altura": 0.4, "Experiencia": 112},
    {"Nombre": "Charizard", "Peso": 90, "Altura": 1.7, "Experiencia": 240},
    {"Nombre": "Bulbasaur", "Peso": 6.9, "Altura": 0.7, "Experiencia": 64},
    {"Nombre": "Squirtle", "Peso": 9, "Altura": 0.5, "Experiencia": 63},
]

# Probar cada algoritmo de ordenamiento
sort_algorithms = {
    "Bubble Sort": BubbleSort(),
    "Quick Sort": QuickSort(),
    "Merge Sort": MergeSort(),
}

for name, algorithm in sort_algorithms.items():
    sorter = PokemonSorter(algorithm)
    sorted_data = sorter.sort(pokemon_data, "Experiencia")
    
    print(f"\n{name} ordenado por Experiencia:")
    for p in sorted_data:
        print(p)
