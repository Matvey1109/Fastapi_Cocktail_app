from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.cocktail.api import get_ingredients_of_cocktail, get_random_cocktail

router = APIRouter(
    prefix="/cocktail",
    tags=["Cocktail"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("", response_class=HTMLResponse)
def get_cocktail(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("base.html", context=context)


@router.get("/get_cocktail", response_class=HTMLResponse)
def get_cocktail(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("get_cocktail.html", context=context)


@router.get("/get_cocktail/{name_of_cocktail}", response_class=HTMLResponse)
def get_cocktail_info(request: Request, name_of_cocktail: str):
    info = get_ingredients_of_cocktail(name_of_cocktail)
    context = {
        "cocktail": info,
        "request": request
    }
    return templates.TemplateResponse("index.html", context=context)


@router.get("/random_cocktail", response_class=HTMLResponse)
def get_random_cocktail_info(request: Request):
    info = get_random_cocktail()
    context = {
        "cocktail": info,
        "request": request
    }
    return templates.TemplateResponse("random.html", context=context)
