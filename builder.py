import random, json

lixeiras = {
    'quantidade': 205,
    'capacidade': 1000,
    'tamanho': 3,
}

localizacoes = { 'quantidade': 458 }

habitacoes = { 'quantidade': 801 }

distanciaMaxima = 300

# monta dados

espacos = map(
    lambda i: '%s %s' % (i, 30),
    range(1, localizacoes['quantidade'] + 1)
)

volumes = map(
    lambda i: '%s %s' % (i, 0),
    range(1, localizacoes['quantidade'] + 1)
)

capacidades = map(
    lambda i: '%s %s' % (i, lixeiras['capacidade']),
    range(1, lixeiras['quantidade'] + 1)
)

tamanhos = map(
    lambda i: '%s %s' % (i, lixeiras['tamanho']),
    range(1, lixeiras['quantidade'] + 1)
)

dados = json.loads(open('./distancias.json').read())
distancias = map(
    lambda i: '    %s\t\t%s' % (i, '\t'.join(map(
        lambda j: str(round(dados[str(i - 1)][str(j - 1)])),
        range(1, habitacoes['quantidade'] + 1)
    ))),
    range(1, localizacoes['quantidade'] + 1)
)

ajuste_habitacoes = map(
    lambda i: str(i),
    range(1, habitacoes['quantidade'] + 1)
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
%s;
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
