import json
from bin_model import BinModel

input_file = open('./testes/teste1.json')
data = json.loads(input_file.read())
input_file.close()

solutions = []
objectives = set({})

bin_model = BinModel(data)
first_result = bin_model.solve()

solutions.append(first_result)
objectives.add(json.dumps(first_result['objectives']))

bin_model = BinModel(data)
last_result = bin_model.solve(reverse=True)

last_result['objectives'].reverse()
objectives.add(json.dumps(last_result['objectives']))


diff = last_result['objectives'][0] - first_result['objectives'][0]
for tolerance in range(1, diff):
    solution = BinModel(data).solve(tolerance)
    stringObjective = json.dumps(solution['objectives'])

    if stringObjective not in objectives:
        objectives.add(stringObjective)
        solutions.append(solution)

solutions.append(last_result)

print(solutions)
