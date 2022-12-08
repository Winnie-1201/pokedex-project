from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
# from .pokemonType import MyEnum

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

db = SQLAlchemy()


class Pokemon(db.Model):
    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.Enum("fire",
                             "electric",
                             "normal",
                             "ghost",
                             "psychic",
                             "water",
                             "bug",
                             "dragon",
                             "grass",
                             "fighting",
                             "ice",
                             "flying",
                             "poison",
                             "ground",
                             "rock",
                             "steel",), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounterRate = db.Column(db.Numeric(
        precision=3, scale=2), nullable=False, default=1.00)
    catchRate = db.Column(db.Numeric(
        precision=3, scale=2), nullable=False, default=1.00)
    captured = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime(
        timezone=True), nullable=False, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime(
        timezone=True), nullable=False, server_default=func.current_timestamp())

    items = db.relationship("Item", back_populates="pokemon", cascade="all, delete")


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    pokemon_id = db.Column(db.Integer, db.ForeignKey(
        "pokemons.id"), nullable=False)

    created_at = db.Column(db.DateTime(
        timezone=True), nullable=False, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime(
        timezone=True), nullable=False, server_default=func.current_timestamp())

    pokemon = db.relationship("Pokemon", back_populates="items")

    def to_dict(self):
        return {
            "id": self.id,
            "happiness": self.happiness,
            "image_url": self.image_url,
            "name": self.name,
            "price": self.price
        }
