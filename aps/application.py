
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api, Blueprint, abort

app = Flask('aps')
app.config.from_object('aps.config.DevelopmentConfig')
db = SQLAlchemy(app)
api = Api(app)

import aps.aquarium.models
if app.config['FLASK_ENV'] in ('development', 'testing'):
    db.create_all(app=app)
    a = aps.aquarium.models.Aquarium(name="Aquario Amazonico", ph=6.8)
    db.session.add(a)
    db.session.commit()

import aps.aquarium.views
app.register_blueprint(aps.aquarium.views.bp)