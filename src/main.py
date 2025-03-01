from fastapi import FastAPI
from src.api import health
from src.api.v1.routes import user_routes

app = FastAPI()

app.include_router(health.router)
app.include_router(user_routes.router, prefix="/v1")
