from flask import Blueprint, request
from app.models import Pokemon

pokemons_routes = Blueprint('pokemons', __name__)

@pokemons_routes.route('/')
def get_all_pokemons():
    print('all pokemons route')
    print(Pokemon)
    pokemons = Pokemon.query.all()
    for p in pokemons:
        print(p.to_dict())
    return {"pokemons": []}
