import random, json

bins = {
    'quantity': 205,
    'capacity': 1000,
    'size': 3,
}

locations = {
    'quantity': 458,
    'space': 30,
}

dwellings = { 'quantity': 801 }

distanceData = json.loads(open('./distances.json').read())
volumeData = json.loads(open('./volumes.json').read())

maxDistance = 300

# monta dados

spaces = map(
    lambda i: '%s %s' % (i, locations['space']),
    range(1, locations['quantity'] + 1)
)

capacities = map(
    lambda i: '%s %s' % (i, bins['capacity']),
    range(1, bins['quantity'] + 1)
)

sizes = map(
    lambda i: '%s %s' % (i, bins['size']),
    range(1, bins['quantity'] + 1)
)

volumes = map(
    lambda i: '%s %s' % (i, round(volumeData[i - 1])),
    range(1, dwellings['quantity'] + 1)
)

distances = map(
    lambda i: '    %s\t\t%s' % (i, '\t'.join(map(
        lambda j: str(round(distanceData[str(i - 1)][str(j - 1)])),
        range(1, dwellings['quantity'] + 1)
    ))),
    range(1, locations['quantity'] + 1)
)

dwellingsString = map(
    lambda i: str(i),
    range(1, dwellings['quantity'] + 1)
)

# imprime arquivo

file = open('teste.mod', 'w')
file.write('''data;

param pn := %s;
param ln := %s;
param hn := %s;

param e := %s;
param c := %s;
param t := %s;
param v := %s;
param d :   %s   :=
%s;
param DM %s;

end;
''' % (
    locations['quantity'],
    bins['quantity'],
    dwellings['quantity'],
    ', '.join(spaces),
    ', '.join(capacities),
    ', '.join(sizes),
    ', '.join(volumes),
    '\t'.join(dwellingsString),
    '\n'.join(distances),
    maxDistance
))
file.close()
