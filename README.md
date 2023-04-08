# Ingestão API Síndrome Gripal Brasil


## Passo a Passo
1. Definição do Problema
2. Obtenção dos Dados
3. Exploração dos Dados
4. Preparação dos Dados
5. Armazenamento dos Dados
6. Apresentação dos Dados


## 1. Definição do Problema
#### explicar sobre a api e elasticsearch
A partir da ingestão de uma API Pública do OpenDataSUS que está no Elastic Search, será realizada uma análise inicial para compreender a API, após será realizada a exploratória dos dados, o tratamento dos dados e o armazenamento dos dados tratados e, por fim, a plotagem de tabelas e gráficos como resultado final.


Devido ao início do outono brasileiro em 2023 e a melhora aparente dos casos de COVID-19, surge a questão do aumento de casos de Covid-19 na próxima estação. Como questões norteadoras desta projeto, foram colocadas:
* Questões Principais:
<li> Quantas são as notificações dos casos de síndrome gripal neste momento: no Brasil e em São Paulo?</li>
<li> Será que haverá um aumento de notificações de síndrome gripal com o inverno? </li>

* Questões secundárias:
<li> Quais são os principais testes para detecção de COVID utilizados no país?</li>

## 2. Obtenção dos Dados
Segundo o site do Elastic Search (https://www.elastic.co/pt/what-is/elasticsearch), o Elasticsearch é um mecanismo de busca e análise de dados distribuído, gratuito e aberto para todos os tipos de dados, incluindo textuais, numéricos, geoespaciais, estruturados e não estruturados. É desenvolvido sobre o Apache Lucene e foi lançado pela primeira vez em 2010 pela Elasticsearch N.V. (agora conhecida como Elastic). Conhecido por suas REST APIs simples, natureza distribuída, velocidade e escalabilidade, o Elasticsearch é o componente central do Elastic Stack, um conjunto de ferramentas gratuitas e abertas para ingestão, enriquecimento, armazenamento, análise e visualização de dados. Comumente chamado de ELK Stack (pelas iniciais de Elasticsearch, Logstash e Kibana), o Elastic Stack agora inclui uma rica coleção de agentes lightweight conhecidos como Beats para enviar dados ao Elasticsearch.<br>

Os dados serão coletados a partir de sua API: https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-api-elasticsearch<br>

Segundo o site do Elasticsearch, ele armazena dados como documentos JSON. Cada documento correlaciona um conjunto de chaves (nomes de campos ou propriedades) aos seus valores correspondentes (strings, números, boolianos, datas, matrizes de valores, geolocalizações ou outros tipos de dados).

O Elasticsearch usa uma estrutura de dados chamada índice invertido, que é projetada para permitir buscas de texto completo muito rápidas. Um índice invertido lista cada palavra exclusiva que apareça em qualquer documento e identifica todos os documentos em que cada palavra aparece.

Durante o processo de indexação, o Elasticsearch armazena documentos e desenvolve um índice invertido para tornar os dados dos documentos buscáveis praticamente em tempo real. A indexação é iniciada com a API de índice, pela qual você pode adicionar ou atualizar um documento JSON em um índice específico.

Para aprender sobre a utilização desta API foi necessário procurar por outras fontes além da documentação do Elastic Search, dentre eles:
* Documentação Elastic Search: https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-body.html
* Manual da API da Campanha Nacional de Vacinação da Covid-19, https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao/resource/84707ab9-8497-4f2f-8a0d-b873489a63bf
* MANUAL DE INTEGRAÇÃO - e-SUS NOTIFICA, https://datasus.saude.gov.br/wp-content/uploads/2022/02/Manual-de-Utilizacao-da-API-e-Sus-Notifica.pdf
* Dicionário de Dados, https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-api-elasticsearch/resource/9a2632b2-65b5-4fb0-89d8-2d421e34d4d5

O OpenData SUS recomenda que seja utilizado o site Postman (https://www.postman.com/) para realizar a ingestão da API.<br>
Neste projeto, o site foi utilizado por vezes para realizar a tradução da requisição para a linguagem Python e obtenção dos dados. Contudo, não foi utilizado em nenhuma outra etapa. A biblioteca pandas da linguagem Python foi a responsável pela importação dos dados para o notebook Jupyter.<br>



## 3. Exploração dos Dados
Após realizar a extração dos dados da API para o Jupyter, foi iniciada a fase de exploração dos dados.
Nesta fase a biblioteca Pandas

## 4. Preparação dos Dados

## 5. Armazenamento dos Dados


## 6. Apresentação dos Dados

## Andamento do Projeto
Em Andamento.<br>
Data de Entrega: 12/04/2023.
