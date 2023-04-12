# Notificações Compulsórias de Síndrome Gripal associado ao Covid-19 no Brasil
A partir da ingestão de uma API Pública do OpenDataSUS que está no Elastic Search, será realizada uma análise inicial para compreender a API e, então, será realizada a exploração, o tratamento e o armazenamento dos dados tratados. Esses dados serão analisados eserão apresentados a partir de tabelas e gráficos.<br>

O Elasticsearch é um mecanismo de busca e análise distribuído, de código aberto, que permite armazenar, buscar e analisar grandes volumes de dados de forma eficiente e em tempo real. É comumente utilizado para indexar e pesquisar dados em tempo real, como logs, métricas, dados de aplicativos e muito mais.<br>

A API do Elasticsearch permite interagir com o Elasticsearch usando várias linguagens de programação, como Python, Java, PHP, entre outras. A API aceita solicitações HTTP e responde com dados em formato JSON. O JSON (JavaScript Object Notation) é um formato de dados leve, legível por humanos e amplamente utilizado para representar dados estruturados. É uma notação de valor-chave, onde os dados são representados em pares de chave e valor, que podem ser aninhados em estruturas hierárquicas.<br>

## Ferramentas Utilizadas
Desenvolvido com:<br>
<li>Anaconda, https://www.anaconda.com/;</li>
<li>Notebook Jupyter, https://jupyter.org/</li>
<li>Utilizada linguagem Python 3.9, instaladas Bibliotecas Pandas, Matplotlib, Json, Requests, Datetime;</li>
<li>Dados das notificações compulsórias de Síndromes Gripais, https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-api-elasticsearch;</li>
<li>Postman, https://www.postman.com/</li>

### Acessando o Projeto

1. Anaconda/ Jupyter<br>

Clonar este repositório para o seu Github.<br>
Importar o repositório para uma pasta de seu computador.<br>
Realizar a instalação do programa Anaconda, instalar o Python 3.9 e, dentro de Anaconda Navigator, realizar o download do Jupyter.<br>

No prompt do Anaconda, realizar o download das bibliotecas Pandas, Matplotlib, Json, Requests, Datetime.<br>
Abrir Jupyter Notebook no Anaconda.<br>
Procurar pela pasta do repositório.<br>
Abrir o arquivo 'SindromeGripal_API.ipynb',<br>
Apertar em 'RUN'.<br>
Após este passo, o programa irá rodar todos o projeto.<br>

2) Google Colab<br>

Caso não deseje clonar todo esse repositório, também será disponibilizado um arquivo no Google Colab.<br>
Você só precisará clicar no link abaixo e clicar em "Ambiente de execução" e, em seguida, "Executar tudo".<br>

<a class="nav-link" href="" target="_blank"></a><br>


## Passo a Passo
1. Definição do Problema<br>
2. Obtenção dos Dados<br>
3. Exploração dos Dados<br>
4. Preparação dos Dados<br>
5. Armazenamento dos Dados<br>
6. Apresentação dos Dados<br>

## 1. Definição do Problema
Devido ao início do outono brasileiro em 2023 e a melhora aparente dos casos de COVID-19, surge a preocupação com o aumento de casos de Covid-19 neste ano.
Será preciso utilizarmos máscara novamente para ir ao mercado?<br>
Será que é seguro sairmos para as festas?<br>
Será que é preciso nos atentarmos novamente com a ventilação dos ambientes?<br>
Posso cumprimentar as pessoas com beijo no rosto?<br>

Todas essas questões remetem à preocupação do retorno do Covid-19 e um cuidado com nossos entes queridos...

Para acompanharmos estas dúvidas, colocamos como questões da pesquisa:<br>
* Questões Principais:<br>
<li> Quantas são as notificações diárias dos casos de síndrome gripal neste momento: no Brasil e em São Paulo?</li>
<li> Será que haverá um aumento de notificações de síndrome gripal associadas ao Covid-19 com a chegada do tempo frio? </li>

* Questões secundárias:<br>
<li> Quais são os principais testes para detecção de COVID utilizados no país?</li>

## 2. Obtenção dos Dados
Os dados serão coletados a partir da API do Elastic Search: https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-api-elasticsearch<br>

Para aprender sobre a utilização desta API foi necessário procurar por outras fontes além da documentação do Elastic Search, dentre eles:
* Documentação Elastic Search: https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-body.html
* Manual da API da Campanha Nacional de Vacinação da Covid-19, https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao/resource/84707ab9-8497-4f2f-8a0d-b873489a63bf
* MANUAL DE INTEGRAÇÃO - e-SUS NOTIFICA, https://datasus.saude.gov.br/wp-content/uploads/2022/02/Manual-de-Utilizacao-da-API-e-Sus-Notifica.pdf
* Dicionário de Dados, https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-api-elasticsearch/resource/9a2632b2-65b5-4fb0-89d8-2d421e34d4d5

O OpenData SUS recomenda que seja utilizado o site Postman para realizar a ingestão da API.<br>
Neste projeto, o site foi utilizado por vezes para realizar a tradução da requisição para a linguagem Python e obtenção dos dados. Contudo, não foi utilizado em nenhuma outra etapa. A biblioteca pandas da linguagem Python foi a responsável pela importação dos dados para o notebook Jupyter e por toda a exploração, tratamento e armazenamento dos dados.<br>

<img src="img/obtencao_dados.jpg" alt="Etapa 2">

## 3. Exploração dos Dados
Após realizar a extração dos dados da API para o Jupyter, foi iniciada a fase de exploração dos dados.<br>
Nesta fase, a biblioteca Pandas será utilizada para realização da análise exploratória dos dados.<br>

<img src="img/prep.trat_dados.jpg" alt="Etapa 3">


## 4. Preparação dos Dados
Nesta fase, os dados serão tratados e filtrados baseados nos problemas colocados anteriormente. Primordialmente, biblioteca pandas será utilizada nesta fase. <br>
<img src="img/prep.trat_dados.jpg" alt="Etapa 4">


## 5. Armazenamento dos Dados
Nesta fase, será realizado o armazenamento dos dados em um arquivo CSV para que seja possível realizar a apresentação dos dados posteriormente.<br>

<img src="img/armazenamento_dados.jpg" alt="Etapa 5">

## 6. Apresentação dos Dados
A apresentação dos dados será realizada a partir de um arquivo Power BI.<br>

<img src="img/powerbi.jpg" alt="Etapa 6">


## Andamento do Projeto
Em Andamento.<br>
Data de Entrega: 12/04/2023.
