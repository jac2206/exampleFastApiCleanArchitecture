from src.application.use_cases.user_service import UserService
from src.application.use_cases.user_service_db import UserServiceDB
from src.application.use_cases.auth_service import AuthService
from src.application.use_cases.pokemon_service import PokemonService
from src.infraestructure.repositories.user_repository import UserRepository
from src.infraestructure.adapter.pokeapi_adapter import PokemonAdapter
from src.infraestructure.http_client import HttpClient
from src.infraestructure.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

def auth_service():
    return AuthService()

def http_client():
    return HttpClient()

def user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)

def user_service(auth_service: AuthService = Depends(auth_service)):  
    return UserService(auth_service)  # 👈 Se inyecta la dependencia

def user_service_db(user_repository: UserRepository = Depends(user_repository)):
    return UserServiceDB(user_repository)

def pokemon_adapter(http_client: HttpClient = Depends(http_client)):
    return PokemonAdapter(http_client)

def pokemon_service(pokemon_adapter: PokemonAdapter = Depends(pokemon_adapter)):
    return PokemonService(pokemon_adapter)
