import pandas as pd
# Datos ordenados de ejemplo (puedes reemplazarlos con los que obtuviste de la API)
datos_ordenados = {
    "Seleccion": [5, 7, 23, 32, 34, 62],
    "Burbuja": [5, 7, 23, 32, 34, 62],
    "Inserción": [5, 7, 23, 32, 34, 62],
    "Merge Sort": [5, 7, 23, 32, 34, 62],
    "Quick Sort": [5, 7, 23, 32, 34, 62],
    "Heap Sort": [5, 7, 23, 32, 34, 62],
    "Counting Sort": [5, 7, 23, 32, 34, 62],
    "Radix Sort": [5, 7, 23, 32, 34, 62],
    "Bucket Sort": [5, 7, 23, 32, 34, 62]
}

# Convertir los datos en un DataFrame de pandas
df = pd.DataFrame(datos_ordenados)

# Guardar el DataFrame en un archivo Excel
nombre_archivo = "datos_ordenados.xlsx"
df.to_excel(nombre_archivo, index=False)

print(f"Datos guardados en {nombre_archivo} con éxito!")
