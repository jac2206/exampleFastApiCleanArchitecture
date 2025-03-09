import os
from dotenv import load_dotenv

# Cargar variables de entorno una sola vez
load_dotenv()

class Config:
    DB_SERVER = os.getenv("DB_SERVER")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_PORT = os.getenv("DB_PORT")
    BASE_URL_POKEAPI = os.getenv("BASE_URL_POKEAPI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    API_KEY = os.getenv("API_KEY")

    @staticmethod
    def get_database_url():
        # print(f"mssql+pymssql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_SERVER}:{Config.DB_PORT}/{Config.DB_NAME}")
        return f"mssql+pymssql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_SERVER}:{Config.DB_PORT}/{Config.DB_NAME}"
