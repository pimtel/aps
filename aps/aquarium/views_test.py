from unittest import TestCase

import pytest

from aps import application
from aps.aquarium.models import Aquarium


@pytest.fixture(scope='class')
def app():
    app = application.create_app()
    with app.app_context():
      application.db.create_all()
    return app


@pytest.fixture(scope='class')
def client(request, app):
    request.cls.client = app.test_client()


@pytest.fixture(scope='class')
def db(request, app):
    with app.app_context():
      request.cls.db = application.db
      yield

@pytest.mark.usefixtures('client')
@pytest.mark.usefixtures('db')
class BaseTestCase(TestCase):
  pass


class AquariumTest(BaseTestCase):

  def setUp(self):
    a = Aquarium(name="Aquario Amazonico", ph=6.8)
    self.db.session.add(a)
    self.db.session.commit()

  def test_get_aquariums(self):
    res = self.client.get('/aquariums/')
    assert res.json[0]['name'] == 'Aquario Amazonico'


class AquariumEmptyTest(BaseTestCase):

  def test_get_empty_aquariums(self):
    res = self.client.get('/aquariums/')
    assert res.json == []
