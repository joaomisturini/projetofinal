import json
from locationModel import LocationModel

locationModel = LocationModel(json.loads(open('./input.json').read()))
print(locationModel.solve())
