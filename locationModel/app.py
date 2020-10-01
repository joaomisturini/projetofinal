import json
from location_model import LocationModel

input_file = open('./teste.json')
data = json.loads(input_file.read())
input_file.close()

locations = data['locations']
dwellings = data['dwellings']

data['locations'] = list(map(lambda location: {
    'installed': int(location['volume'] > 0),
}, locations))
data['dwellings_count'] = len(dwellings)

location_model = LocationModel(data)
result = location_model.solve()

for i in range(len(locations)):
    locations[i]['residents'] = 0

    if (locations[i]['volume'] == 0):
        continue

    for j in range(len(dwellings)):
        if (result['designated_locations'][i][j] == 0):
            continue

        locations[i]['residents'] += dwellings[j]['residents']

for i in range(len(dwellings)):
    if (dwellings[i]['residents'] == 0):
        dwellings[i]['volume'] = 0
        continue

    for j in range(len(locations)):
        if (result['designated_locations'][j][i] == 1):
            dwellings[i]['volume'] = locations[j]['volume'] * (
                dwellings[i]['residents'] / locations[j]['residents']
            )
            break

print(locations, dwellings)
