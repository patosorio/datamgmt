# Initialise the Flask App

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialise the database instance
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    db.init_app(app)
    migrate.init_app(app, db)

    # blueprint setup
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

