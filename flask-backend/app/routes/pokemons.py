from flask import Blueprint, request
from app.models import Pokemon
import random

pokemons_routes = Blueprint('pokemons', __name__)


@pokemons_routes.route('/')
def get_all_pokemons():
    print('all pokemons route')
    print(Pokemon)
    ls = []
    pokemons = Pokemon.query.all()
    for p in pokemons:
        print(p.to_dict())
        ls.append(p.to_dict())
        print(ls)
    return {"pokemons": ls}


@pokemons_routes.route('/types')
def get_types():
    ls = []
    pokemons = Pokemon.query.all()
    for p in pokemons:
        print(p.to_dict()['type'])
        ls.append(p.to_dict()['type'])

    return {"pokemons_types": ls}


@pokemons_routes.route('/random')
def get_random_pokemon():
    ls = []
    pokemons = Pokemon.query.all()
    for p in pokemons:
        print(p.to_dict())
        ls.append(p.to_dict())
        print(ls)
    return {"random_pokemons": random.choice(ls)}

@pokemons_routes.route('/battle')
def get_pokemons_battle():
    ls=[]
    pokemons = Pokemon.query.all()
    for p in pokemons:
        print(p.to_dict())
        ls.append(p.to_dict())

    [index1,index2] = random.sample(range(0,100),2)
    # print(index1,index2)

    return [ls[index1],ls[index2]]
