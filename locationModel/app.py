import json
from locationModel import LocationModel

location_model = LocationModel(json.loads(open('./input.json').read()))
print(location_model.solve())
