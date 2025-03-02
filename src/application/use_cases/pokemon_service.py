from typing import List, Optional
from src.domain.entity.user import User
from src.application.dto.user_dto import UserDTO
from src.core.base_service import BaseService
from src.infraestructure.adapter.pokeapi_adapter import PokemonAdapter

class PokemonService(BaseService):  # ✅ Hereda de BaseService
    def __init__(self, pokemon_adapter: PokemonAdapter):
        # self
        self.pokemon_adapter = pokemon_adapter

    def get_pokemon(self, pokemon: str):
        return self.execute(lambda: self.pokemon_adapter.fetch_pokemon(pokemon))