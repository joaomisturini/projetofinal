from docplex.mp.model import Model
from docplex.util.environment import get_environment

# DADOS

locations = [
    { 'space': 10 },
    { 'space': 8 },
    { 'space': 6 },
    { 'space': 6 },
]

bins = [
    {
        'capacity': 2,
        'size': 1.5,
    },
    {
        'capacity': 2,
        'size': 1.5,
    },
    {
        'capacity': 2,
        'size': 1.5,
    },
    {
        'capacity': 2,
        'size': 1.5,
    },
    {
        'capacity': 2,
        'size': 1.5,
    },
    {
        'capacity': 2,
        'size': 1.5,
    },
]

dwellings = [
    { 'volume': 1 },
    { 'volume': 1 },
    { 'volume': 1 }
]

distances = [
    [ 25, 90, 25 ],
    [ 90, 70, 90 ],
    [ 20, 90, 90 ],
    [ 90, 25, 90 ],
]

maxDistance = 100

# MODELO

model = Model(name='Lixeiras')
model.installed = model.binary_var_matrix(len(locations), len(bins), 'lixeiras_instaladas')
model.designated = model.binary_var_matrix(len(locations), len(dwellings), 'localizacoes_designadas')

# constraint lim_volume
for i in range(len(locations)):
    sumBins = model.sum(bins[j]['capacity'] * model.installed[ (i, j) ] for j in range(len(bins)))
    sumDwellings = model.sum(dwellings[j]['volume'] * model.designated[ (i, j) ] for j in range(len(dwellings)))
    model.add_constraint(sumBins >= sumDwellings, 'lim_volume_%s' % i)

# constraint lim_espaco
for i in range(len(locations)):
    summation = model.sum(bins[j]['size'] * model.installed[ (i, j) ] for j in range(len(bins)))
    model.add_constraint(summation <= locations[i]['space'], 'lim_espaco_%s' % i)

# constraint lim_localizacao
for i in range(len(dwellings)):
    summation = model.sum(model.designated[ (j, i) ] for j in range(len(locations)))
    model.add_constraint(summation == 1, 'lim_localizacao_%s' % i)

# constraint lim_lixeiras
for i in range(len(locations)):
    for j in range(len(dwellings)):
        summation = model.sum(model.installed[ (i, k) ] for k in range(len(bins)))
        model.add_constraint(summation >= model.designated[ (i, j) ], 'lim_lixeiras_%s_%s' % (i, j))

# constraint lim_distancia
for i in range(len(locations)):
    for j in range(len(dwellings)):
        setDistance = distances[i][j] * model.designated[ (i, j) ]
        model.add_constraint(setDistance <= maxDistance, 'lim_distancia_%s_%s' % (i, j))

# constraint lim_instalacao
for i in range(len(bins)):
    summation = model.sum(model.installed[ (j, i) ] for j in range(len(locations)))
    model.add_constraint(summation <= 1, 'lim_instalacao_%s' % i)

# objective distancia
distanceObj = model.sum(
    distances[i][j] * model.designated[ (i, j) ] for j in range(len(dwellings)) for i in range(len(locations))
)
model.add_kpi(distanceObj, 'distancia')

# objective lixeiras
binsObj = model.sum(
    model.installed[ (i, j) ] for j in range(len(bins)) for i in range(len(locations))
)
model.add_kpi(binsObj, 'lixeiras')

model.minimize_static_lex([ distanceObj, binsObj ], reltols=0)

# RESOLVE O PROBLEMA

if model.solve():
    # print(model.kpi_value_by_name('distancia'))
    # print(model.kpi_value_by_name('lixeiras'))
    print(model.solution.multi_objective_values)

    for i in range(len(locations)):
        for j in range(len(bins)):
            key = 'lixeiras_instaladas_%s_%s' % (i, j)
            print(key, model.solution.get_value(key))

    for i in range(len(locations)):
        for j in range(len(dwellings)):
            key = 'localizacoes_designadas_%s_%s' % (i, j)
            print(key, model.solution.get_value(key))
else:
    print('infeasible')
