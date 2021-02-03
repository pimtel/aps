import pytest

from faker import Faker

from aps.aquarium.models import Aquarium

faker = Faker()


@pytest.fixture
def generate_model(request):

  def _(self, size, name=None):
    name = name or faker.name()
    return [self.mixer.blend(Aquarium, name=name, ph=faker.random_number(digits=1, fix_len=2)) for _ in range(size)]

  request.cls.generate_model = _
