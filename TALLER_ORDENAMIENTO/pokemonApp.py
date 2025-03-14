import tkinter as tk
from tkinter import ttk
from ApiRequest import ApiRequest
from bubbleSort import BubbleSort
from quickSort import QuickSort
from mergeSort import MergeSort
from pokemonSorter import PokemonSorter

class PokemonSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon-Dongo")
        self.root.configure(bg="#282c34")

        # Fetch data from API
        self.api_client = ApiRequest("https://pokeapi.co/api/v2/pokemon?limit=20")
        self.data = self.api_client.fetchData()

        # Sorting strategies
        self.bubble_sort = BubbleSort()
        self.quick_sort =  QuickSort()
        self.merge_sort = MergeSort()

        # UI Elements
        self.sort_label = tk.Label(root, text="Seleccione el método de ordenamiento:", bg="#282c34", fg="white", font=("Helvetica", 12))
        self.sort_label.pack(pady=5)

        self.sort_method = ttk.Combobox(root, values=["Bubble Sort", "Quick Sort", "Merge Sort"], state="readonly")
        self.sort_method.pack(pady=5)

        self.column_label = tk.Label(root, text="Seleccione la columna:", bg="#282c34", fg="white", font=("Helvetica", 12))
        self.column_label.pack(pady=5)

        self.column_choice = ttk.Combobox(root, values=["Nombre", "Peso", "Altura", "Experiencia"], state="readonly")
        self.column_choice.pack(pady=5)

        self.sort_button = tk.Button(root, text="Ordenar", command=self.sort_data, bg="#61afef", fg="white", font=("Helvetica", 10, "bold"), relief="flat")
        self.sort_button.pack(pady=10)

        # Treeview for displaying data
        self.tree = ttk.Treeview(root, columns=("Nombre", "Peso", "Altura", "Experiencia"), show="headings", height=15)
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Peso", text="Peso")
        self.tree.heading("Altura", text="Altura")
        self.tree.heading("Experiencia", text="Experiencia")
        self.tree.pack(pady=10)

        # Show original data
        self.display_data(self.data)

    def display_data(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for pokemon in data:
            self.tree.insert("", tk.END, values=(pokemon['Nombre'], pokemon['Peso'], pokemon['Altura'], pokemon['Experiencia']))

    def sort_data(self):
        method = self.sort_method.get()
        column = self.column_choice.get()

        if method == "Bubble Sort":
            sorter = PokemonSorter(self.bubble_sort)
        elif method == "Quick Sort":
            sorter = PokemonSorter(self.quick_sort)
        elif method == "Merge Sort":
            sorter = PokemonSorter(self.merge_sort)
        else:
            return

        if column:
            sorted_data = sorter.sort(self.data, column)
            self.display_data(sorted_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonSorterApp(root)
    root.mainloop()
