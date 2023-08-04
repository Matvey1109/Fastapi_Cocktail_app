from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.cocktail.router import router as router_cocktail

app = FastAPI()
app.mount("/src/static", StaticFiles(directory="src/static"), name="static")

app.include_router(router_cocktail)
