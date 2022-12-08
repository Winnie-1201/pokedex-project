import enum
from sqlalchemy import Enum

types = [
    "fire",
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
    "steel",
]

class MyEnum(enum.Enum):
    types = types


