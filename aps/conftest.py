from unittest import TestCase

import pytest

from aps import application


@pytest.fixture
def app():
    app = application.create_app()
    with app.app_context():
      application.db.create_all()
    return app


@pytest.fixture
def client(request, app):
    request.cls.client = app.test_client()


@pytest.fixture
def db(request, app):
    with app.app_context():
      request.cls.db = application.db
      yield


@pytest.fixture
def mixer(request, app):
    with app.app_context():
      from mixer.backend.flask import mixer
      mixer.init_app(app)
      request.cls.mixer = mixer
      yield


@pytest.mark.usefixtures('client', 'db', 'mixer')
class BaseTestCase(TestCase):
  pass
