import os
from flask import Flask
from flask_smorest import Api, Blueprint, abort
from flask_sqlalchemy import SQLAlchemy

FLASK_CONFIG_OBJECT_NAMESPACE = os.environ['FLASK_CONFIG_OBJECT_NAMESPACE']

db = SQLAlchemy()
api = Api()


def create_app():
    app = Flask('aps')
    app.config.from_object(FLASK_CONFIG_OBJECT_NAMESPACE)
    api.init_app(app)
    db.init_app(app)

    import aps.aquarium.views
    app.register_blueprint(aps.aquarium.views.bp)

    return app
