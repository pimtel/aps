import marshmallow as ma


class AquariumSerializer(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String(required=True)
    ph = ma.fields.Float(required=True)


class DriftWoodSerializer(ma.Schema):
    specie = ma.fields.String(required=True)
    weight = ma.fields.Float(required=True)
    treated = ma.fields.Bool(default=True)

class RockSerializer(ma.Schema):
    name = ma.fields.String(required=True)
    change_ph = ma.fields.Bool(default=False)
    change_to = ma.fields.Str(validate=ma.validate.OneOf(['alkaline', 'newtral', 'none', 'acid']))

class AquascapingSerializer(ma.Schema):
    driftwood = ma.fields.Nested(DriftWoodSerializer)
    rock = ma.fields.Nested(RockSerializer)

class AquascapingAquariumSerializer(ma.Schema):
    aquarium = ma.fields.Nested(AquariumSerializer)
    detail = ma.fields.Nested(AquascapingSerializer)