# Otimização cíclica do posicionamento de lixeiras inteligentes

Este projeto contém o código fonte e testes do otimizador cíclico de posicionamento de lixeiras inteligentes, desenvolvido com Python e CPLEX Optimizer. A otimização é realizada através dos objetivos de redução na distância entre as lixeiras e as habitações e na redução da quantidade de lixeiras instaladas. A solução criada é composta em dois módulos, que são responsáveis pelo posicionamento dos contentores de resíduos (`binModel`) e pela atualização das habitações e suas estimativas de geração de resíduos (`locationModel`), cobrindo não somente o posicionamento inicial das lixeiras, mas também possíveis reposicionamentos periódicos e cíclicos.

## BinModel

O módulo `binModel` é responsável por definir o posicionamento das lixeiras inteligentes. Recebendo os dados relativos à uma área em estudo (como um bairro ou um município) como as distancias entre as habitações e localizações candidatas, entre outros, o algoritmo busca encontrar uma solução ótima para a posição das lixeiras, com base na tolerância informada pelo usuário. Como resultado, obtém-se a lista de posições onde as mesmas devem ser instaladas, iniciando também a coleta de informações sobre geração de resíduos nestas localizações.

## LocationModel

Criado para ser executado em etapa posterior, o módulo `locationModel` busca atualizar as habitações no modelo e suas estimativas de geração de resíduos, considerando os dados obtidos a partir da instalação de lixeiras inteligentes. Para isto, o módulo deve receber as listas de habitações e de localizações de lixeiras. Como resultado, são obtidos dados atualizados de geração de resíduos por habitação, considerando a quantidade residentes em cada moradia.

## Requisitos

* Python 3.0+
* CPLEX Optimizer 12.9+
