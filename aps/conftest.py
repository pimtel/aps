from unittest import TestCase

import pytest

from aps import application


@pytest.fixture(scope='class', autouse=True)
def app():
    app = application.create_app()
    with app.app_context():
      application.db.create_all()
    return app


@pytest.fixture(scope='class', autouse=True)
def client(request, app):
    request.cls.client = app.test_client()


@pytest.fixture(scope='class', autouse=True)
def db(request, app):
    with app.app_context():
      request.cls.db = application.db
      yield


@pytest.mark.usefixtures('client', 'db')
class BaseTestCase(TestCase):
  pass
