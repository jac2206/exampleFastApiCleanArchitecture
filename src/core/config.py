import os
from dotenv import load_dotenv

# Cargar variables de entorno una sola vez
load_dotenv()

class Config:
    DB_SERVER = os.getenv("DB_SERVER", "localhost")
    DB_NAME = os.getenv("DB_NAME", "mi_basedatos")
    DB_USER = os.getenv("DB_USER", "sa")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "supersegura")
    DB_PORT = os.getenv("DB_PORT", "1433")

    @staticmethod
    def get_database_url():
        # print(f"mssql+pymssql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_SERVER}:{Config.DB_PORT}/{Config.DB_NAME}")
        return f"mssql+pymssql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_SERVER}:{Config.DB_PORT}/{Config.DB_NAME}"
