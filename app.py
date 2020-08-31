from docplex.mp.model import Model

# DADOS

localizacoes = [
    {
        'espaco': 10,
        'volume': 3
    },
    {
        'espaco': 8,
        'volume': 4
    },
    {
        'espaco': 6,
        'volume': 0
    },
    {
        'espaco': 6,
        'volume': 0
    },
]

lixeiras = [
    {
        'capacidade': 2,
        'tamanho': 1.5
    },
    {
        'capacidade': 2,
        'tamanho': 1.5
    },
    {
        'capacidade': 2,
        'tamanho': 1.5
    },
    {
        'capacidade': 2,
        'tamanho': 1.5
    },
    {
        'capacidade': 2,
        'tamanho': 1.5
    },
    {
        'capacidade': 2,
        'tamanho': 1.5
    },
]

total_habitacoes = 3

distancias = [
    [ 25, 90, 25 ],
    [ 90, 70, 90 ],
    [ 20, 90, 90 ],
    [ 90, 25, 90 ],
]

distancia_maxima = 100

# MODELO

model = Model(name='Lixeiras')
model.instaladas = model.binary_var_matrix(len(localizacoes), len(lixeiras), 'lixeiras instaladas')
model.designadas = model.binary_var_matrix(len(localizacoes), total_habitacoes, 'localizaces designadas')

# constraint lim_volume
for i in range(len(localizacoes)):
    somatorio = model.sum(lixeiras[j]['capacidade'] * model.instaladas[ (i, j) ] for j in range(len(lixeiras)))
    model.add_constraint(somatorio >= localizacoes[i]['volume'], 'lim_volume_%s' % i)

# constraint lim_espaco
for i in range(len(localizacoes)):
    somatorio = model.sum(lixeiras[j]['tamanho'] * model.instaladas[ (i, j) ] for j in range(len(lixeiras)))
    model.add_constraint(somatorio <= localizacoes[i]['espaco'], 'lim_espaco_%s' % i)

# constraint lim_localizacao
for i in range(total_habitacoes):
    somatorio = model.sum(model.designadas[ (j, i) ] for j in range(len(localizacoes)))
    model.add_constraint(somatorio == 1, 'lim_localizacao_%s' % i)

# constraint lim_lixeiras
for i in range(len(localizacoes)):
    for j in range(total_habitacoes):
        somatorio = model.sum(model.instaladas[ (i, k) ] for k in range(len(lixeiras)))
        model.add_constraint(somatorio >= model.designadas[ (i, j) ], 'lim_lixeiras_%s_%s' % (i, j))

# constraint lim_distancia
for i in range(len(localizacoes)):
    for j in range(total_habitacoes):
        calculo = distancias[i][j] * model.designadas[ (i, j) ]
        model.add_constraint(calculo <= distancia_maxima, 'lim_distancia_%s_%s' % (i, j))

# constraint lim_instalacao
for i in range(len(lixeiras)):
    somatorio = model.sum(model.instaladas[ (j, i) ] for j in range(len(localizacoes)))
    model.add_constraint(somatorio <= 1, 'lim_instalacao_%s' % i)

# objective distancia
obj_distancia = model.sum(
    distancias[i][j] * model.designadas[ (i, j) ] for j in range(total_habitacoes) for i in range(len(localizacoes))
)
model.add_kpi(obj_distancia, 'distancia')

# objective lixeiras
obj_lixeiras = model.sum(
    model.instaladas[ (i, j) ] for j in range(len(lixeiras)) for i in range(len(localizacoes))
)
model.add_kpi(obj_lixeiras, 'lixeiras')

model.minimize_static_lex([ obj_distancia, obj_lixeiras ], reltols=0)

# RESOLVE O PROBLEMA

if model.solve():
    # model.report()
    print(model.kpi_value_by_name('distancia'))
    print(model.kpi_value_by_name('lixeiras'))
else:
    print('infeasible')
