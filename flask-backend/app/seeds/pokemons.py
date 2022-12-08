from app.models import db, Pokemon, environment, SCHEMA

from .pokemon_data import pokemon


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
        db.session.add(new_pokemon)
        db.session.commit()


def undo_pokemon():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.pokemons RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM pokemons")

    db.session.commit()
