from aps.application import db

class Aquarium(db.Model):
    __tablename__ = 'aquariums'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    ph = db.Column(db.Float)

    def __repr__(self):
        return f'<Aquarium {self.name}>'


class AquariumFromDynamo:
    def __init__(self, aquarium):
        self.id = aquarium.id
        self.name = aquarium.name
        self.ph = aquarium.ph