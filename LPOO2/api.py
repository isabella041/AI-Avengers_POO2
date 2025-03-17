import requests
import json

class ApiRequest:
    def __init__(self, base_url: str):
        """Inicializa la clase con la URL base de la API."""
        self._base_url = base_url

    def get_url(self) -> str:
        """Devuelve la URL base."""
        return self._base_url

    def fetch_data(self):
        """Hace la petición a la API y devuelve los datos en una lista de diccionarios."""
        response = requests.get(self._base_url)

        if response.status_code == 200:
            response_dict = json.loads(response.text)
            pokemon_list = response_dict.get("results", [])

            data = []  # Lista para almacenar la información de los Pokémon

            for pokemon in pokemon_list:
                pokemon_data = requests.get(pokemon['url']).json()

                data.append({
                    'Nombre': pokemon_data['name'],
                    'Peso': pokemon_data['weight'],
                    'Altura': pokemon_data['height'],
                    'Experiencia': pokemon_data['base_experience']
                })

            return data

        return []  # Si falla la petición, devuelve una lista vacía
