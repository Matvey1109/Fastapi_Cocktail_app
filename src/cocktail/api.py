import requests
from pprint import pprint


def get_ingredients_of_cocktail(name_of_cocktail: str):
    api = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
                       f"{name_of_cocktail}").json()["drinks"][0]
    ingredients: list[str] = []
    for key in api.keys():
        if "Ingredient" in key and api[key] is not None:
            ingredients.append(api[key])

    info = {"Name": api["strDrink"], "Category": api["strCategory"], "Photo": api["strDrinkThumb"],
            "Instruction": api["strInstructions"], "Ingredients": ingredients}
    return info


def get_random_cocktail():
    api = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/random.php").json()["drinks"][0]

    ingredients: list[str] = []
    for key in api.keys():
        if "Ingredient" in key and api[key] is not None:
            ingredients.append(api[key])

    info = {"Name": api["strDrink"], "Category": api["strCategory"], "Photo": api["strDrinkThumb"],
            "Instruction": api["strInstructions"], "Ingredients": ingredients}
    return info
