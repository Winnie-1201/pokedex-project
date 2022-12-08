from flask import Blueprint, request

from app.models import db, Pokemon
from app.forms import PokemonForm
import random

pokemons_routes = Blueprint('pokemons', __name__)


@pokemons_routes.route('')
def get_all_pokemons():
    pokemons = Pokemon.query.all()
    return [p.to_dict() for p in pokemons]


@pokemons_routes.route('', methods=['POST'])
def add_pokemon():
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_pokemon = Pokemon(
            number=form.data["number"],
            imageUrl=form.data["imageUrl"],
            name=form.data["name"],
            attack=form.data["attack"],
            defense=form.data["defense"],
            type=form.data["type"],
            moves=str(form.data["moves"]),
            captured=form.data["captured"] if "captured" in form.data else False
        )
        try:
            db.session.add(new_pokemon)
            db.session.commit()
            return new_pokemon.to_dict()

        except Exception as error:
            db.session.rollback()
            errors = []
            for e in error.args:
                errors.append(e)
            return {'errors': errors}, 401

    errors = []
    if form.errors:
        print(form.errors)
        for e in form.errors:
            errors.append(f"{e}: {form.errors[e][0]}")
    return {'errors': errors}, 401


@pokemons_routes.route('/<int:id>', methods=['PUT'])
def update_pokemon(id):
    print('put route')
    print(id)
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        print(form.data)
        pokemon = Pokemon.query.get(id)
        pokemon.number = form.data["number"]
        pokemon.attack = form.data["attack"]
        pokemon.defense = form.data["defense"]
        pokemon.imageUrl = form.data["imageUrl"]
        pokemon.name = form.data["name"]
        pokemon.type = form.data["type"]
        pokemon.moves = form.data["moves"]

        try:
            db.session.commit()
            return pokemon.to_dict()

        except Exception as error:
            db.session.rollback()
            errors = []
            for e in error.args:
                errors.append(e)
            return {'errors': errors}, 401

    errors = []
    if form.errors:
        print(form.errors)
        for e in form.errors:
            errors.append(f"{e}: {form.errors[e][0]}")
    return {'errors': errors}, 401


# @pokemons_routes.route('/')
# def get_all_pokemons():
#    print('all pokemons route')
#    print(Pokemon)
#    ls = []
#    pokemons = Pokemon.query.all()
#    for p in pokemons:
#        print(p.to_dict())
#        ls.append(p.to_dict())
#        print(ls)
#    return {"pokemons": ls}


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
