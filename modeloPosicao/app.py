import json
from binModel import BinModel

binModel = BinModel(json.loads(open('./input.json').read()))
print(binModel.solve(0))
