from flask.views import MethodView
from flask_smorest import Blueprint

from aps.application import db
from aps.aquarium.models import Aquarium, AquariumFromDynamo
from aps.aquarium.serializers import AquariumSerializer, AquascapingAquariumSerializer
from aps.aquarium import hanlders

bp = Blueprint(
    'aquariums',
    'aquariums',
    url_prefix='/aquariums',
    description='Operation on aquariums'
)


@bp.route('/')
class AquariumsResource(MethodView):

    @bp.response(AquariumSerializer(many=True))
    def get(self):
        return Aquarium.query.all()

    @bp.arguments(AquariumSerializer)
    @bp.response(AquariumSerializer, code=201)
    def post(self, aquarium):
        new_aquarium = Aquarium(**aquarium)
        db.session.add(new_aquarium)
        db.session.commit()
        return new_aquarium


@bp.route('/<aquarium_id>')
class AquariumByIdResource(MethodView):

    @bp.response(AquariumSerializer)
    def get(self, aquarium_id):
        aquarium = Aquarium.query.get_or_404(aquarium_id)
        return AquariumFromDynamo(aquarium)

    @bp.response(code=204)
    def delete(self, aquarium_id):
        aquarium = Aquarium.query.get_or_404(aquarium_id)
        db.session.delete(aquarium)
        db.session.commit()


@bp.route('/<aquarium_id>/aquascaping')
class AquascapingAquariumResource(MethodView):

    @bp.response(AquascapingAquariumSerializer)
    def get(self, aquarium_id):
        aquarium = Aquarium.query.get_or_404(aquarium_id)
        return hanlders.build_aquascaping_from_aquarium(aquarium)
