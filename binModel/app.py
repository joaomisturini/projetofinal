import json
from binModel import BinModel

bin_model = BinModel(json.loads(open('./testes/teste1.json').read()))
print(bin_model.solve(0))
