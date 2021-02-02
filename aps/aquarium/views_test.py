import pytest

from aps.aquarium.models import Aquarium
from aps.conftest import BaseTestCase


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
