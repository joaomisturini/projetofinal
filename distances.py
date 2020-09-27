import json, geopy.distance

houses = json.loads(open('./dados/casas.geojson').read())['features']
housesLength = len(houses)
buildings = json.loads(open('./dados/edificios.geojson').read())['features']
buildingsLength = len(buildings)
locations = json.loads(open('./dados/localizacoes.geojson').read())['features']
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

open('./distances.json', 'w').write(json.dumps(distances))
