from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name
from flask.app import Flask

db = SQLAlchemy()


def create_app(config_name: str) -> Flask:
    print(f"Config name => {config_name}")
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    return app
