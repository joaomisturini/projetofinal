import json
from docplex.mp.model import Model

# DADOS

data = json.loads(open('./input.json').read())

distances = data['distances']
dwellingsCount = data['dwellingsCount']
locations = data['locations']

# MODELO

model = Model(name='Localizacoes')
model.designated = model.binary_var_matrix(len(locations), dwellingsCount, 'localizacoes_designadas')

# constraint lim_localizacao
for i in range(dwellingsCount):
    summation = model.sum(model.designated[ (j, i) ] * locations[j]['installed'] for j in range(len(locations)))
    model.add_constraint(summation == 1, 'lim_localizacao_%s' % i)

# objective distancia
distanceObj = model.sum(
    distances[i][j] * model.designated[ (i, j) ] for j in range(dwellingsCount) for i in range(len(locations))
)
model.add_kpi(distanceObj, 'distancia')

model.minimize(distanceObj)

# RESOLVE O PROBLEMA

if model.solve():
    # print(model.kpi_value_by_name('distancia'))
    print(model.solution.multi_objective_values)

    for i in range(len(locations)):
        for j in range(dwellingsCount):
            chave = 'localizacoes_designadas_%s_%s' % (i, j)
            print(chave, model.solution.get_value(chave))
else:
    print('infeasible')
