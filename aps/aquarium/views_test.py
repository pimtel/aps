import pytest

from faker import Faker

from aps.aquarium.models import Aquarium
from aps.conftest import BaseTestCase

faker = Faker()


@pytest.mark.usefixtures('generate_model')
class AquariumTest(BaseTestCase):

  def test_get_aquariums(self):
    aquariums = self.generate_model(3, name='Aquario Amazonico')
    [self.db.session.add(aquarium) for aquarium in aquariums]
    self.db.session.commit()
    res = self.client.get('/aquariums/')
    self.assertEqual(res.json[0]['name'],'Aquario Amazonico')

  def test_exists_three(self):
    res = self.client.get('/aquariums/')
    self.assertIsInstance(res.json, list)


class AquariumEmptyTest(BaseTestCase):

  def test_get_empty_aquariums(self):
    res = self.client.get('/aquariums/')
    assert res.json == []
