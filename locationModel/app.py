import json
from locationModel import LocationModel

location_model = LocationModel(json.loads(open('./testes/teste1.json').read()))
print(location_model.solve())
