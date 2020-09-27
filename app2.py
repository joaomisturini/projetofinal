from docplex.mp.model import Model

# DADOS

localizacoes = [
    { 'instalada': 1 },
    { 'instalada': 0 },
    { 'instalada': 1 },
    { 'instalada': 1 },
]

total_habitacoes = 4

distancias = [
    [ 25, 90, 25, 90 ],
    [ 90, 70, 90, 25 ],
    [ 20, 90, 90, 90 ],
    [ 90, 25, 90, 90 ],
]

# MODELO

model = Model(name='Localizacoes')
model.designadas = model.binary_var_matrix(len(localizacoes), total_habitacoes, 'localizacoes_designadas')

# constraint lim_localizacao
for i in range(total_habitacoes):
    somatorio = model.sum(model.designadas[ (j, i) ] * localizacoes[j]['instalada'] for j in range(len(localizacoes)))
    model.add_constraint(somatorio == 1, 'lim_localizacao_%s' % i)

# objective distancia
obj_distancia = model.sum(
    distancias[i][j] * model.designadas[ (i, j) ] for j in range(total_habitacoes) for i in range(len(localizacoes))
)
model.add_kpi(obj_distancia, 'distancia')

model.minimize(obj_distancia)

# RESOLVE O PROBLEMA

if model.solve():
    # print(model.kpi_value_by_name('distancia'))
    print(model.solution.multi_objective_values)

    for i in range(len(localizacoes)):
        for j in range(total_habitacoes):
            chave = 'localizacoes_designadas_%s_%s' % (i, j)
            print(chave, model.solution.get_value(chave))
else:
    print('infeasible')
