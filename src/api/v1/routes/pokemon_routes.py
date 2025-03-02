from typing import List
from fastapi import APIRouter, Depends
from src.core.dependencies import pokemon_service
from src.application.use_cases.pokemon_service import PokemonService

router = APIRouter()

@router.get("/{pokemon}")
def get_pokemon(pokemon: str ,pokemon_service: PokemonService = Depends(pokemon_service)):  
    pokemon_service = pokemon_service.get_pokemon(pokemon)
    return pokemon_service

