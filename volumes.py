import json

city = {
    'dwellings': 9193,
    'population': 30241,
    'ratio': 3.289568149679104, # quantidade de pessoas por habitação
    'amount': 1.0975000826692238, # em litros
}

houses = json.loads(open('./dados/casas.geojson').read())['features']
buildings = json.loads(open('./dados/edificios.geojson').read())['features']

volumes = []

for i in range(len(houses)):
    volumes.append(city['ratio'] * city['amount'])

for i in range(len(buildings)):
    descricao = buildings[i]['properties']['description']
    apartamentos = float(descricao.split()[0])
    volumes.append(apartamentos * city['ratio'] * city['amount'])

open('./volumes.json', 'w').write(json.dumps(volumes))
