from fastapi import FastAPI, Request
from src.api import health
from src.api.v1.routes import user_routes as user_router_v1
from src.api.v2.routes import user_routes as user_router_v2
from fastapi.responses import JSONResponse
import logging
import os
from src.core.config import Config
from colorama import Fore, Style, init

app = FastAPI()

# Imprimir variables de entorno con colores
print(Fore.CYAN + "🔹 Variables de entorno cargadas:" + Style.RESET_ALL)
for key, value in os.environ.items():
    if key.startswith("DB_"):  # Opcional: Filtrar solo las relevantes
        print(Fore.YELLOW + key + ": " + Fore.GREEN + value + Style.RESET_ALL)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Manejo global de excepciones no controladas"""
    logging.error(f"Excepción no manejada: {str(exc)} en {request.url}")
    return JSONResponse(
        status_code=500,
        content={"message": "Ocurrió un error inesperado en el servidor"}
    )
    

app.include_router(health.router)
app.include_router(user_router_v1.router, prefix="/v1/user", tags=["User V1"])
app.include_router(user_router_v2.router, prefix="/v2/user", tags=["Users V2"])
