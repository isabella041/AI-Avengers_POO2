import requests
import json
import pandas as pd

# URL de la API
url = "https://www.datos.gov.co/resource/sbcs-4d5y.json"

# Obtener los datos de la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    datos = response.json()
    df = pd.DataFrame(datos)  # Convertir a DataFrame de pandas
    print("✅ Datos obtenidos correctamente de la API")
else:
    print("❌ Error al obtener los datos:", response.status_code)


