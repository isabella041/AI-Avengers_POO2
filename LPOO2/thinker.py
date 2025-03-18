import tkinter as tk
from tkinter import ttk
from api import ApiRequest
from burbuja import BubbleSort
from quick import QuickSort
from merge import MergeSort
from pokemon import PokemonSorter
from selection import SelectionSort
from insertion import InsertionSort
from heap import HeapSort
from counting import CountingSort
from radix import RadixSort
from bucket import BucketSort

class PokemonSorterApp:
    def __init__(self, root):
        print("Interfaz iniciando...")  # Mensaje de depuración
        self.root = root
        self.root.title("Pokemon-Dongo")
        self.root.configure(bg="#282c34")

        # Obtener datos de la API
        self.api_client = ApiRequest("https://pokeapi.co/api/v2/pokemon?limit=20")
        self.data = self.api_client.fetch_data()

        # Inicializar algoritmos de ordenamiento
        self.algorithms = {
            "Bubble Sort": BubbleSort(),
            "Quick Sort": QuickSort(),
            "Merge Sort": MergeSort(),
            "Selection Sort": SelectionSort(),
            "Insertion Sort": InsertionSort(),
            "Heap Sort": HeapSort(),
            "Counting Sort": CountingSort(),
            "Radix Sort": RadixSort(),
            "Bucket Sort": BucketSort()
        }

        # UI - Selección de método de ordenamiento
        self.sort_label = tk.Label(root, text="Seleccione el método de ordenamiento:",
                                   bg="#282c34", fg="white", font=("Helvetica", 12))
        self.sort_label.pack(pady=5)

        self.sort_method = ttk.Combobox(root, values=list(self.algorithms.keys()), state="readonly")
        self.sort_method.pack(pady=5)

        # UI - Selección de columna para ordenar
        self.column_label = tk.Label(root, text="Seleccione la columna:",
                                     bg="#282c34", fg="white", font=("Helvetica", 12))
        self.column_label.pack(pady=5)

        self.column_choice = ttk.Combobox(root, values=["Peso", "Altura", "Experiencia"], state="readonly")
        self.column_choice.pack(pady=5)

        # UI - Selección del orden
        self.order_label = tk.Label(root, text="Seleccione el orden:", 
                                    bg="#282c34", fg="white", font=("Helvetica", 12))
        self.order_label.pack(pady=5)

        self.order_choice = ttk.Combobox(root, values=["Ascendente", "Descendente"], state="readonly")
        self.order_choice.pack(pady=5)
        self.order_choice.current(0)  # Seleccionar "Ascendente" por defecto

        # Botón de ordenamiento
        self.sort_button = tk.Button(root, text="Ordenar", command=self.sort_data,
                                     bg="#61afef", fg="white", font=("Helvetica", 10, "bold"), relief="flat")
        self.sort_button.pack(pady=10)

        # Tabla de datos
        self.tree = ttk.Treeview(root, columns=("Nombre", "Peso", "Altura", "Experiencia"), show="headings", height=15)
        for col in ("Nombre", "Peso", "Altura", "Experiencia"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack()

    def sort_data(self):
        """Ordena los datos según la selección del usuario."""
        method = self.sort_method.get()
        column = self.column_choice.get()
        order = self.order_choice.get()  # Obtener el orden seleccionado

        if method and column:
            sorter = PokemonSorter(self.algorithms[method])

            # Determinar si el orden es descendente
            reverse = True if order == "Descendente" else False

            sorted_data = sorter.sort(self.data, column, reverse)

            # Limpiar la tabla antes de insertar nuevos datos
            for row in self.tree.get_children():
                self.tree.delete(row)

            # Insertar los datos ordenados en la tabla
            for pokemon in sorted_data:
                self.tree.insert("", "end", values=(pokemon["Nombre"], pokemon["Peso"], pokemon["Altura"], pokemon["Experiencia"]))
        else:
            print("Seleccione un método, una columna y el orden antes de ordenar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonSorterApp(root)
    root.mainloop()
