# Otimizador de posicionamento de lixeiras inteligentes

Este projeto contém o código fonte e testes do módulo otimizador de posicionamento de lixeiras inteligentes,
desenvolvido com Python e CPLEX Optimizer. A otimização é realizada através dos objetivos de redução na distância entre
as lixeiras e as habitações e na redução da quantidade de lixeiras instaladas. A solução criada é composta em dois
módulos, que são responsáveis pelo posicionamento dos contentores de resíduos (`binModel`) e pela atualização das
habitações e suas estimativas de geração de resíduos (`locationModel`), cobrindo não somente o posicionamento inicial
das lixeiras, mas também possíveis reposicionamentos periódicos.

## Requisitos

* Python 3.0+
* CPLEX Optimizer 12.9+
