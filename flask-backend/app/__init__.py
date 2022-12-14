
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask
import os
from .models import db
from .config import Config
from flask_migrate import Migrate
from .seeds import seed_commands


from .api.items import item_routes
from app.routes.pokemons import pokemons_routes



app = Flask(__name__)

app.cli.add_command(seed_commands)
app.config.from_object(Config)



app.register_blueprint(pokemons_routes, url_prefix='/api/pokemon')
app.register_blueprint(item_routes, url_prefix="/api/items")


db.init_app(app)
Migrate(app, db)


# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
