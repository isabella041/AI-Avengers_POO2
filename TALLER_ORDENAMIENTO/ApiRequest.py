import requests
import json

class ApiRequest():
    def __init__(self, baseUrl: str):
        self._base_url = baseUrl
    
    def getUrl(self) -> str:
        return self._base_url
    
    def fetchData(self):
        response = requests.get(self._base_url)
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            pokemon_list = response_dict.get("results", [])

            # Lista para almacenar los datos
            data = []

            # Hacer una petición por cada Pokémon
            for pokemon in pokemon_list:
                pokemon_data = requests.get(pokemon['url']).json()
                data.append({
                    'Nombre': pokemon_data['name'],
                    'Peso': pokemon_data['weight'],
                    'Altura': pokemon_data['height'],
                    'Experiencia': pokemon_data['base_experience']
                })

            return data
        
    

url = "https://pokeapi.co/api/v2/pokemon?limit=20"
cliente = ApiRequest(url)

# Convertir a lista de listas
pokemon_data = cliente.fetchData()
