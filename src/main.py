from fastapi import FastAPI, Request
from src.api import health
from src.api.v1.routes import user_routes
from fastapi.responses import JSONResponse
import logging

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Manejo global de excepciones no controladas"""
    logging.error(f"Excepción no manejada: {str(exc)} en {request.url}")
    return JSONResponse(
        status_code=500,
        content={"message": "Ocurrió un error inesperado en el servidor"}
    )

app.include_router(health.router)
app.include_router(user_routes.router, prefix="/v1")
