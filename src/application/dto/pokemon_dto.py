from pydantic import BaseModel

class PokemonDTO(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    types: list[str]
