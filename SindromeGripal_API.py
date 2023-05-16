#!/usr/bin/env python
# coding: utf-8

# ## 1. Definição do Problema
# 
# 

# A realização de notificações de Síndromes Gripais são obrigatórias para todos os casos suspeitos de Covid-19 e devem ser enviadas até 24 horas após a ocorrência de suspeita ou confirmação de doença, agravo ou evento de saúde pública. 
# 
# Os dados utilizados neste estudo são oriundos do sistema e-SUS NOTIFICA, que foi desenvolvido para registro de casos de Síndrome Gripal suspeitos de Covid-19, e contém dados referentes ao local de residência do paciente (campos: estado, município), independentemente de terem sido notificados em outro estado ou município (Campos: estadoNotificação, municípioNotificação), além de demográficos e clínicos epidemiológicos dos casos.
# 

# ### Questões Principais:<br>
# <li> Quantas são as notificações dos casos de síndrome gripal neste momento: no Brasil e em São Paulo?</li>
# 
# ### Questões secundárias:<br>
# <li> Quais são os principais testes para detecção de COVID utilizados no país?</li>
# <li> Quais são os principais sintomas listados na notificação dos casos?</li>
# <li> Está ocorrendo um aumento dos casos de Covid-19 no Brasil?</li>

# ## 2. Obtenção dos Dados
# Iremos realizar a importação das bibliotecas que serão utilizadas e, também, a ingestão da API locada no ElasticSearch com os dados de Notificações de Síndromes Gripais do Brasil.

# In[1]:


import requests
import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt
from datetime import date

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# URL com Todos os Estados, /count
url = 'https://elasticsearch-saps.saude.gov.br/desc-esus-notifica-estado-*/_count'
auth = ('user-public-notificacoes', 'Za4qNXdyQNSa9YaA')

# Notificações BR
r_br = requests.get(url, auth=auth)

if r_br.status_code == 200:
    data_br = r_br.json()
else:
    print(f"Erro na solicitação: {r_br.status_code}")


# In[3]:


# URL com estado de SP, /count
url_sp = 'https://elasticsearch-saps.saude.gov.br/desc-esus-notifica-estado-sp/_count'
auth = ('user-public-notificacoes', 'Za4qNXdyQNSa9YaA')

# Notificações SP

r_sp = requests.get(url_sp, auth=auth)

if r_sp.status_code == 200:
    data_sp = r_sp.json()
else:
    print(f"Erro na solicitação: {r_sp.status_code}")


# In[4]:


# Importação BR Sintomas
# URL com Todos os Estados, /search, scroll (sintomas)
url_sint = "https://elasticsearch-saps.saude.gov.br/desc-esus-notifica-estado-*/_search?scroll=1m"

payload = json.dumps({
  "size": 10000,
  "_source": [
    "sintomas"
  ],
  "query": {
    "bool": {
      "filter": {
        "exists": {
          "field": "sintomas"
        }
      }
    }
  }
})
headers = {
  'Authorization': 'Basic dXNlci1wdWJsaWMtbm90aWZpY2Fjb2VzOlphNHFOWGR5UU5TYTlZYUE=',
  'Content-Type': 'application/json'
}

r_sint_br = requests.request("POST", url_sint, headers=headers, data=payload)

if r_sint_br.status_code == 200:
    data_bra = r_sint_br.json()
else:
    print(f"Erro na solicitação: {r_sint_br.status_code}")


# In[5]:


#URL com todos os Estados, /search (testes e diário)
url_testes = "https://elasticsearch-saps.saude.gov.br/desc-esus-notifica-estado-*/_search"

# Importação Testes BR
payload = json.dumps({
  "track_total_hits": True,
  "size": 0,
  "query": {
    "term": {
      "registroAtual": {
        "value": True
      }
    }
  },
  "aggs": {
    "TopTestes": {
      "terms": {
        "field": "testes.tipoTeste.keyword",
        "size": 10
      }
    }
  }
})
headers = {
  'Authorization': 'Basic dXNlci1wdWJsaWMtbm90aWZpY2Fjb2VzOlphNHFOWGR5UU5TYTlZYUE=',
  'Content-Type': 'application/json'
}

r_testes_br = requests.request("POST", url_testes, headers=headers, data=payload)

if r_testes_br.status_code == 200:
    data_testes = r_testes_br.json()
else:
    print(f"Erro na solicitação: {r_testes_br.status_code}")


# In[6]:


#URL com todos os Estados, /search (testes e diário)
url_testes = "https://elasticsearch-saps.saude.gov.br/desc-esus-notifica-estado-*/_search"

# Importação diário BR
payload = json.dumps({
  "track_total_hits": True,
  "size": 0,
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "@timestamp": {
              "gte": "2021-08-20T00:00:00Z",
              "lte": "now",
              "time_zone": "-03:00"
            }
          }
        },
        {
          "term": {
            "registroAtual": {
              "value": True
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "AtualizacaoDia": {
      "date_histogram": {
        "field": "@timestamp",
        "interval": "day"
      }
    }
  }
})
headers = {
  'Authorization': 'Basic dXNlci1wdWJsaWMtbm90aWZpY2Fjb2VzOlphNHFOWGR5UU5TYTlZYUE=',
  'Content-Type': 'application/json'
}

r_dia_br = requests.request("GET", url_testes, headers=headers, data=payload)

if r_dia_br.status_code == 200:
    data_dias = r_dia_br.json()
else:
    print(f"Erro na solicitação: {r_dia_br.status_code}")


# ## Etapas 3-5: Exploração, Preparação e Armazenamento dos Dados
# Estas etapas serão realizadas todas em conjunto para que possamos organizar por informação e não por etapas e, com isso, possamos iniciar e terminar cada informação de uma só vez e o leitor possa visualizar e compreender o processo.
# 
# De maneira geral, a etapa de exploração é onde iremos explorar os dados e visualizar de que maneira eles estão dispostos.
# Já a etapa de preparação dos dados é quando iremos tratar os dados e transformá-los em um dataframe em que os dados estarão mais fáceis de serem analisados.
# 
# Na etapa de armazenamento, iremos guardar a informação tratada para não perdermos a informação e, também, podermos realizar estudos comparatórios (nos casos das notificações diárias, por exemplo, podemos verificar se houve ou não um aumento no número de notificações de um dia para o outro).

# ## Total de notificações

# #### Exploração e Preparação dos Dados

# In[7]:


# Normaliza o objeto JSON para um DataFrame
data_br = pd.json_normalize(data_br)


# In[8]:


# Exibe a mensagem com o total de notificações no Brasil
total_notificacoes = data_br['count'][0]
print(f"O total de notificações no Brasil é de {total_notificacoes}.")


# In[9]:


# Cria um DataFrame com o valor total de notificações
df_br = pd.DataFrame({'Total de Notificações': [total_notificacoes]})
display(df_br)
#df_br.to_csv(r'data\total_br.csv', index=False)


# In[10]:


# Inserindo a data no dataframe
data = date.today().strftime('%Y-%m-%d')

# Cria um DataFrame com o valor total de notificações
df_br = pd.DataFrame({'Total de Notificações': [total_notificacoes], 'Data':[data]})
display(df_br)



# In[11]:


# Atualização dos dados em arquivo CSV: neste passo iremos atualizar os novos dados no arquivo CSV existente

# Leitura dos arquivos
notificacoes_br = pd.read_csv(r'data\total_br.csv')
novas_notif_br = df_br

notificacoes_br = pd.concat([notificacoes_br, novas_notif_br], ignore_index=True)

# Remover linhas duplicadas
notificacoes_br = notificacoes_br.drop_duplicates(subset='Data')
display(notificacoes_br)
notificacoes_br.to_csv(r'data\total_br.csv', index=False)


# In[12]:


data_sp = pd.json_normalize(data_sp)


# In[13]:


# Exibe a mensagem com o total de notificações em São Paulo
total_notificacoes_sp = data_sp['count'][0]
print(f"O total de notificações em São Paulo é de {total_notificacoes_sp}.")


# In[14]:


# Inserindo a data no dataframe
data = date.today().strftime('%Y-%m-%d')

# Cria um DataFrame com o valor total de notificações
df_sp = pd.DataFrame({'Total de Notificações': [total_notificacoes_sp], 'Data':[data]})
display(df_sp)


# In[15]:


# Atualização dos dados em arquivo CSV: neste passo iremos atualizar os novos dados no arquivo CSV existente

# Leitura dos arquivos
notificacoes_sp = pd.read_csv(r'data\total_sp.csv')
novas_notif_sp = df_sp
notificacoes_sp = pd.concat([notificacoes_sp, novas_notif_sp], ignore_index=True)

# Remover linhas duplicadas
notificacoes_sp = notificacoes_sp.drop_duplicates(subset='Data')
display(notificacoes_sp)
notificacoes_sp.to_csv(r'data\total_sp.csv', index=False)


# ## Sintomas

# #### Exploração e Preparação dos Dados

# In[16]:


data_bra


# In[17]:


data_bra['hits']['hits']


# In[18]:


df_bra = pd.json_normalize(data_bra['hits']['hits'])


# In[19]:


df_bra.columns


# In[20]:


df_bra['_source.sintomas']


# In[21]:


# Tratamento do dataframe sintomas

# Separar os valores da coluna 'sintomas'
df_bra['_source.sintomas'] = df_bra['_source.sintomas'].str.split(r',\s|,')

# Transformar a coluna em uma coluna de lista e separá-la em múltiplas linhas
df_bra = df_bra.explode('_source.sintomas')


# In[22]:


# Contagem das informações de sintomas
df_bra['_source.sintomas'].value_counts()


# In[23]:


# Tratamento de informações iguais
df_bra['_source.sintomas'] = df_bra['_source.sintomas'].replace({'Dispineia': 'Dispneia'})
df_bra['_source.sintomas'] = df_bra['_source.sintomas'].replace({'Outros: Paciente assintomático': 'Paciente assintomático'})


# In[24]:


df_sintomas = df_bra['_source.sintomas'].value_counts()
df_sintomas = pd.DataFrame(df_sintomas)
df_sintomas = df_sintomas.reset_index()
# Renomeando colunas
df_sintomas = df_sintomas.rename(columns={'_source.sintomas': 'Total', 'index': 'Sintomas'}) 


display(df_sintomas)


# #### Armazenamento dos Dados

# In[25]:


# Tratando o dataframe de testes para poder realizar um acompanhamento diário

# Inserindo a data no dataframe
data = date.today().strftime('%Y-%m-%d')
df_sintomas['data'] = data

# Transformando os testes em colunas e os números em linhas
df_sintomas = df_sintomas.pivot(index='data', columns='Sintomas', values='Total')

# Resetando o índice para obter a data como coluna
df_sintomas = df_sintomas.reset_index()

# Renomeando as colunas para o nome dos testes
df_sintomas.columns.name = None
display(df_sintomas)


# In[26]:


# Atualização dos dados em arquivo CSV: neste passo iremos atualizar os novos dados no arquivo CSV existente

# Leitura dos arquivos
notificacoes_sintomas = pd.read_csv(r'data\notificacoes_sintomas.csv')
novas_notif_sintomas = df_sintomas

# Concatenar os DataFrames verticalmente
notificacoes_sintomas = pd.concat([notificacoes_sintomas, novas_notif_sintomas], ignore_index=True)

# Remover linhas duplicadas
notificacoes_sintomas = notificacoes_sintomas.drop_duplicates(subset='data')
display(notificacoes_sintomas)


# ## Testes

# #### Exploração e Preparação dos Dados

# In[27]:


# Explorando dados testes covid - visualização das colunas
df_testes = pd.json_normalize(data_testes)
df_testes.columns


# In[28]:


# Explorando e filtrando dados testes covid 
df_buckets = pd.json_normalize(df_testes['aggregations.TopTestes.buckets'])
df_buckets


# In[29]:


# Transformando dados em dataframe

buckets = df_testes.at[0, 'aggregations.TopTestes.buckets']
df_buckets = pd.DataFrame(columns=['key', 'doc_count'])

# Filtrando dados no dataframe e organizando colunas
for i in range(len(buckets)):
    key_valor = buckets[i]['key']
    doc_count_valor = buckets[i]['doc_count']
    new_row = pd.DataFrame({'key': [key_valor], 'doc_count': [doc_count_valor]})
    df_buckets = pd.concat([df_buckets, new_row], ignore_index=True)

display(df_buckets)


# #### Armazenamento dos Dados

# In[30]:


# Tratando o dataframe de testes para poder realizar um acompanhamento diário

# Inserindo a data no dataframe
data = date.today().strftime('%Y-%m-%d')
df_buckets['data'] = data

# Transformando os testes em colunas e os números em linhas
df_buckets = df_buckets.pivot(index='data', columns='key', values='doc_count')

# Resetando o índice para obter a data como coluna
df_buckets = df_buckets.reset_index()

# Renomeando as colunas para o nome dos testes
df_buckets.columns.name = None
display(df_buckets)



# In[31]:


# Atualização dos dados em arquivo CSV: neste passo iremos atualizar os novos dados no arquivo CSV existente

# Leitura dos arquivos
notificacoes_testes = pd.read_csv(r'data\notificacoes_testes.csv')
novas_notif_testes = df_buckets

# Concatenar os DataFrames verticalmente
notificacoes_testes = pd.concat([notificacoes_testes, novas_notif_testes], ignore_index=True)

# Remover linhas duplicadas
notificacoes_testes = notificacoes_testes.drop_duplicates(subset='data')
display(notificacoes_testes)


# ## Verificação diária das Notificações

# #### Exploração e Preparação dos Dados

# In[32]:


# Explorando dados de notificações diárias
data = json.loads(json.dumps(data_dias))
data


# In[33]:


# Explorando e filtrando dados de notificações diárias
df_dias = pd.json_normalize(data['aggregations']['AtualizacaoDia']['buckets'])
df_dias


# In[34]:


# Criando dataframe para quantidade de notificações diárias
dados = []

for i in range(len(df_dias)):
    key_valor = df_dias.iloc[i]['key_as_string']
    doc_count_valor = df_dias.iloc[i]['doc_count']
    dados.append({'Data': key_valor, 'Total de Notificações': doc_count_valor})

df_notificacoes = pd.DataFrame(dados)

# Tratando coluna Data para datetime
df_notificacoes['Data'] = pd.to_datetime(df_notificacoes['Data'])
df_notificacoes['Data'] = df_notificacoes['Data'].dt.strftime('%d-%m-%Y')

display(df_notificacoes)

df_notificacoes.to_csv(r'data\notificacoes_diarias.csv', index=False)


# #### Armazenamento dos Dados

# In[35]:


# Atualização dos dados em arquivo CSV: neste passo iremos atualizar os novos dados no arquivo CSV existente

# Leitura dos arquivos
notificacoes_diarias = pd.read_csv(r'data\notificacoes_diarias.csv')
novas_notif = df_notificacoes

# Concatenando os DataFrames
notificacoes_diarias = pd.concat([notificacoes_diarias, novas_notif], ignore_index=True)

# Remover linhas duplicadas
notificacoes_diarias = notificacoes_diarias.drop_duplicates(subset='Data')


# In[36]:


# Salvando as novas informações no arquivo CSV

notificacoes_sintomas.to_csv(r'data\notificacoes_sintomas.csv', index=False)
notificacoes_testes.to_csv(r'data\notificacoes_testes.csv', index=False)
notificacoes_diarias.to_csv(r'data\notificacoes_diarias.csv', index=False)


# #### Plotagem dos Dados

# In[37]:


# Plotagem dos dados de notificações diárias para análise rápida
df_notificacoes.plot(x='Data', y='Total de Notificações', kind='line')


# In[ ]:




