import random

lixeiras = {
    'quantidade': 40,
    'capacidade': 3,
    'tamanho': 2,
}

localizacoes = { 'quantidade': 20 }

habitacoes = { 'quantidade': 30 }

distanciaMaxima = 250

# monta dados

espacos = map(
    lambda i: '%s %s' % (i, random.choice(range(4, 20))),
    range(1, localizacoes['quantidade'])
)

volumes = map(
    lambda i: '%s %s' % (i, max(0, random.choice(range(-4, 7)))),
    range(1, localizacoes['quantidade'])
)

capacidades = map(
    lambda i: '%s %s' % (i, lixeiras['capacidade']),
    range(1, lixeiras['quantidade'])
)

tamanhos = map(
    lambda i: '%s %s' % (i, lixeiras['tamanho']),
    range(1, lixeiras['quantidade'])
)

distancias = map(
    lambda i: '    %s\t\t%s' % (i, '\t'.join(map(
        lambda j: str(round(random.choice(range(10, 30)) * (1 + abs(i - j)))),
        range(1, habitacoes['quantidade'])
    ))),
    range(1, localizacoes['quantidade'])
)

ajuste_habitacoes = map(
    lambda i: str(i),
    range(1, habitacoes['quantidade'])
)

# imprime arquivo

file = open('teste.mod', 'w')
file.write('''data;

param pn := %s;
param ln := %s;
param hn := %s;

param e := %s;
param v := %s;
param c := %s;
param t := %s;
param d :   %s   :=
%s
param DM %s;

end;
''' % (
    localizacoes['quantidade'],
    lixeiras['quantidade'],
    habitacoes['quantidade'],
    ', '.join(espacos),
    ', '.join(volumes),
    ', '.join(capacidades),
    ', '.join(tamanhos),
    '\t'.join(ajuste_habitacoes),
    '\n'.join(distancias),
    distanciaMaxima
))
file.close()
