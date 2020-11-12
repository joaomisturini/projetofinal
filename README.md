# Otimização cíclica do posicionamento de lixeiras inteligentes

Este projeto contém o código fonte e testes do otimizador cíclico de posicionamento de lixeiras inteligentes, desenvolvido em AMPL, Python e CPLEX Optimizer. A otimização é realizada através dos objetivos de redução na distância entre as lixeiras e as habitações e de redução da quantidade de lixeiras instaladas. A solução criada é composta em dois módulos, que são responsáveis pelo posicionamento dos contentores de resíduos (`binModel`) e pela atualização das estimativas de geração resíduos por habitação (`locationModel`), cobrindo não somente o posicionamento inicial das lixeiras, mas também posteriores reposicionamentos periódicos e cíclicos.

## Arquitetura da solução

A solução neste repositório foi projetada para execução cíclica, visando a melhoria contínua no posicionamento dos contentores no ambiente e levando em consideração a possibilidade de mudanças como a quantidade de habitações ou variações no volume de geração de resíduos em determinada área. Por isto, é realizada a divisão da execução em dois módulos, permitindo a redesignação de lixeiras para habitações e atualização dos dados de geração de resíduos de forma anterior à reavaliação do posicionamento das lixeiras, conforme demonstra o fluxograma abaixo. Na sequência, os módulos `binModel` e `locationModel` são detalhados, explicitando suas responsabilidades.

![Fluxo de execução](https://raw.githubusercontent.com/joaomisturini/projetofinal/master/images/fluxo.png)

### BinModel

O módulo `binModel` é responsável por definir o posicionamento das lixeiras inteligentes. Recebendo os dados relativos à uma área em estudo (como um bairro ou um município) como as distâncias entre as habitações e localizações candidatas, tamanho disponível nas localizações, tamanho e capacidade dos contentores, entre outros, o algoritmo busca encontrar uma solução ótima para a posição das lixeiras, com base na tolerância informada pelo usuário. A otimização é realizada com foco nos objetivos de reduzir a quantidade de contentetores a serem instalados e as distâncias entre habitações e suas lixeiras designadas. Como resultado, obtém-se a lista de posições onde as mesmas devem ser instaladas, iniciando também a coleta de informações sobre geração de resíduos nestas localizações. Desta forma, a execução em laço da solução com diferentes tolerâncias resulta na obtenção da Eficiência de Pareto do problema em estudo.

### LocationModel

Criado para ser executado em etapa anterior ao `binModel`, o módulo `locationModel` busca atualizar a estimativa de geração de resíduos por habitações no modelo, considerando os dados obtidos a partir da instalação de lixeiras inteligentes e possibilitando a execução cíclica para obtenção da melhoria contínua do posicionamento dos contentores. Para isto, o módulo deve receber as listas de habitações e de localizações de lixeiras, para redefinir a designação entre os mesmos e posteriormente realizar a distribuição proporcional do volume de resíduos coletados. Como resultado, são obtidos dados atualizados de geração de resíduos por habitação, considerando a quantidade residentes em cada moradia. Os resultados obtidos por este algoritmo devem ser utilizados como complemento às entradas do algoritmo do módulo `binModel`, como parte das execuções cíclicas da solução.

## Resultados

Os resultados apresentados pela solução mostram melhoras significativas em comparação ao cenário real do bairro Centro de Carlos Barbosa - RS, que foi avaliado no estudo, onde foi possível obter uma redução de aproximadamente 32% na distância total entre habitações e lixeiras, mantendo o número de lixeiras instaladas. Em relação à literatura recente, a solução foi capaz de gerar resultados de qualidade semelhante, apresentando somente uma ligeira desvantagem em resultados que priorizam a redução drástica no número de contentores. As curvas de resultados e situação atual do bairro citado podem ser observados no gráfico abaixo.

![Comparação de resultados](https://raw.githubusercontent.com/joaomisturini/projetofinal/master/images/resultado.png)

Na avaliação de desempenho, a solução foi capaz de apresentar resultados em tempos menores do que trabalhos da literatura recente, demonstrando ganhos significativos nos cenários testados. Os gráficos abaixo exibem os resultados de tempo de execução em relação ao tamanho do cenário, onde é priorizado o resultado com menor distância total (à esquerda) e com menor quantidade de lixeiras (à direita).

<img src="https://raw.githubusercontent.com/joaomisturini/projetofinal/master/images/posicao-distancia.png" alt="Comparação de desempenho - menor distância total" style="width:49%" />

<img src="https://raw.githubusercontent.com/joaomisturini/projetofinal/master/images/posicao-lixeiras.png" alt="Comparação de desempenho - menor quantidade de lixeiras" style="width:49.8%" />

## Requisitos

* Python 3.0+
* CPLEX Optimizer 12.9+
