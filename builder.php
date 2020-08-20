<?php

$lixeiras = [
    'quantidade' => 30,
    'capacidade' => 3,
    'tamanho' => 2,
];

$localizacoes = [ 'quantidade' => 15 ];

$habitacoes = [ 'quantidade' => 20 ];

$distanciaMaxima = 250;

// monta dados

$espacos = array_map(function ($localizacao, $i) {
    return $i . ' ' . mt_rand(4, 20);
}, $localizacoes, range(1, $localizacoes['quantidade']));

$volumes = array_map(function ($localizacao, $i) {
    return $i . ' ' . max(0, mt_rand(-4, 7));
}, $localizacoes, range(1, $localizacoes['quantidade']));

$capacidades = array_map(function ($i) use ($lixeiras) {
    return $i . ' ' . $lixeiras['capacidade'];
}, range(1, $lixeiras['quantidade']));

$tamanhos = array_map(function ($i) use ($lixeiras) {
    return $i . ' ' . $lixeiras['tamanho'];
}, range(1, $lixeiras['quantidade']));

$distancias = array_map(function ($i) use ($habitacoes) {
    $dados = array_map(function ($j) use ($i) {
        $multiplicador = 1 + abs($i - $j);
        return round(mt_rand(10, 30) * $multiplicador);
    }, range(1, $habitacoes['quantidade']));

    return "    " . $i . "\t\t" . implode("\t", $dados);
}, range(1, $localizacoes['quantidade']));

// imprime arquivo

$dados = "data;

param pn := " . $localizacoes['quantidade'] . ";
param ln := " . $lixeiras['quantidade'] . ";
param hn := " . $habitacoes['quantidade'] . ";

param e := " . implode(', ', $espacos) . ";
param v := " . implode(', ', $volumes) . ";
param c := " . implode(', ', $capacidades) . ";
param t := " . implode(', ', $tamanhos) . ";
param d :   " . implode("\t", range(1, $habitacoes['quantidade'])) . "   :=
" . implode("\n", $distancias) . ";
param DM := " . $distanciaMaxima . ";

end;
";

file_put_contents('teste6.mod', $dados);
