

def build_aquascaping_from_aquarium(aquarium):
    return {
        'aquarium': aquarium,
        'detail': {
            'driftwood': {
                'specie': 'Arueira',
                'weight': 450.78,
                'treated': False
            },
            'rock': {
                'name': 'Dolomita',
                'change_ph': True,
                'change_to': 'alkaline'
            }
        }
    }