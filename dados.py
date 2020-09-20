import json, geopy.distance

city = {
    'dwellings': 9193,
    'population': 30241,
    'ratio': 3.289568149679104, # quantidade de pessoas por habitação
    'amountKg': 0.43849731233167627, # lixo por pessoa/dia, em Kg
    'amountL': 1.0975000826692238, # lixo por pessoa/dia, em litros
}

houses = json.loads(open('./dados/casas.geojson').read())['features']
housesLength = len(houses)
buildings = json.loads(open('./dados/edificios.geojson').read())['features']
buildingsLength = len(buildings)
locations = json.loads(open('./dados/localizacoes-12.geojson').read())['features']
locationsLength = len(locations)

distances = {}

for i in range(locationsLength):
    dwelDistances = {}

    location = locations[i]
    locationCoords = location['geometry']['coordinates']

    for j in range(housesLength):
        house = houses[j]
        houseCoords = house['geometry']['coordinates']

        dwelDistances[j] = geopy.distance.distance(locationCoords, houseCoords).m

    for j in range(buildingsLength):
        building = buildings[j]
        buildingCoords = building['geometry']['coordinates']

        newj = j + housesLength
        dwelDistances[newj] = geopy.distance.distance(locationCoords, buildingCoords).m

    distances[i] = dwelDistances

open('./distancias.json', 'a').write(json.dumps(distances))

# for i in range(len(houses)):
#     print('casa %s' % (i + 1), city['ratio'] * city['amountM3'])

# for i in range(len(buildings)):
#     descricao = buildings[i]['properties']['description']
#     apartamentos = float(descricao.split()[0])

#     m3 = apartamentos * city['ratio'] * city['amountM3']
#     cm3 = m3 * 1000000

#     print('edificio %s' % (i + 1), cm3)
