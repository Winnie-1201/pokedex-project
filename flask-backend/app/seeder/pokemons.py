from app.models import db, Pokemon

from .pokemon_data import pokemon


def seed_pokemon():
    for p in pokemon:
        new_pokemon = Pokemon(
            *p
        )
        db.seesion.add(new_pokemon)
        db.session.commit()


def undo_pokemon():
    db.session.execute("DELETE FROM pokemons")

    db.session.commit()
