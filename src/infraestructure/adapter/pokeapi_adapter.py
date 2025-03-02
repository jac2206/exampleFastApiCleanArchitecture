from src.infraestructure.http_client import HttpClient
from src.core.config import Config

class PokemonAdapter:
    BASE_URL = Config.BASE_URL_POKEAPI

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def fetch_pokemon(self, name: str):
        return self.http_client.get(f"{self.BASE_URL}/pokemon/{name}")

    def fetch_pokemon_list(self, limit: int = 10, offset: int = 0):
        params = {"limit": limit, "offset": offset}
        return self.http_client.get(f"{self.BASE_URL}/pokemon", params=params)
