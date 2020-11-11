# Otimização cíclica do posicionamento de lixeiras inteligentes

Este projeto contém o código fonte e testes do otimizador cíclico de posicionamento de lixeiras inteligentes, desenvolvido em AMPL, Python e CPLEX Optimizer. A otimização é realizada através dos objetivos de redução na distância entre as lixeiras e as habitações e de redução da quantidade de lixeiras instaladas. A solução criada é composta em dois módulos, que são responsáveis pelo posicionamento dos contentores de resíduos (`binModel`) e pela atualização das estimativas de geração resíduos por habitação (`locationModel`), cobrindo não somente o posicionamento inicial das lixeiras, mas também posteriores reposicionamentos periódicos e cíclicos.

## BinModel

O módulo `binModel` é responsável por definir o posicionamento das lixeiras inteligentes. Recebendo os dados relativos à uma área em estudo (como um bairro ou um município) como as distâncias entre as habitações e localizações candidatas, tamanho disponível nas localizações, tamanho e capacidade dos contentores, entre outros, o algoritmo busca encontrar uma solução ótima para a posição das lixeiras, com base na tolerância informada pelo usuário. A otimização é realizada com foco nos objetivos de reduzir a quantidade de contentetores a serem instalados e as distâncias entre habitações e suas lixeiras designadas. Como resultado, obtém-se a lista de posições onde as mesmas devem ser instaladas, iniciando também a coleta de informações sobre geração de resíduos nestas localizações. Desta forma, a execução em laço da solução com diferentes tolerâncias resulta na obtenção da Eficiência de Pareto do problema em estudo.

## LocationModel

Criado para ser executado em etapa anterior ao `binModel`, o módulo `locationModel` busca atualizar a estimativa de geração de resíduos por habitações no modelo, considerando os dados obtidos a partir da instalação de lixeiras inteligentes e possibilitando a execução cíclica para obtenção da melhoria contínua do posicionamento dos contentores. Para isto, o módulo deve receber as listas de habitações e de localizações de lixeiras, para redefinir a designação entre os mesmos e posteriormente realizar a distribuição proporcional do volume de resíduos coletados. Como resultado, são obtidos dados atualizados de geração de resíduos por habitação, considerando a quantidade residentes em cada moradia. Os resultados obtidos por este algoritmo devem ser utilizados como complemento às entradas do algoritmo do módulo `binModel`, como parte das execuções cíclicas da solução.

## Requisitos

* Python 3.0+
* CPLEX Optimizer 12.9+
