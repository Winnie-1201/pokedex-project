from app.models import db, Pokemon, environment, SCHEMA, Item

from .pokemon_data import pokemon
from random import randint, choice
    

def seed_pokemon():
    # p = pokemon[0]
    # new_pokemon = Pokemon(
    #     number=p["number"],
    #     imageUrl=p["imageUrl"],
    #     name=p["name"],
    #     attack=p["attack"],
    #     defense=p["defense"],
    #     type=p["type"],
    #     moves=str(p["moves"]),
    #     captured=p["captured"]
    # )
    for p in pokemon:
        new_pokemon = Pokemon(
            number=p["number"],
            imageUrl=p["imageUrl"],
            name=p["name"],
            attack=p["attack"],
            defense=p["defense"],
            type=p["type"],
            moves=str(p["moves"]),
            captured=p["captured"] if "captured" in p else False
        )

        new_item = Item(
            name=choice(["berry", "egg", "eggplant", "banana", "Adamant", "Crystal"]),
            happiness=randint(1, 100),
            price=randint(1, 100),
            image_url=choice([
                "/images/pokemon_berry.svg",
                "/images/pokemon_egg.svg",
                "/images/pokemon_potion.svg",
                "/images/pokemon_super_potion.svg",
            ]),
        )
        new_item.pokemon = new_pokemon

        db.session.add(new_pokemon)
        db.session.commit()


def undo_pokemon():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.pokemons RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM pokemons")

    db.session.commit()
    
