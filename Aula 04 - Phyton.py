# -*- coding: utf-8 -*-
"""
Funcional e OO
Aula 04
Data Sciense com  Pandas
Vanessa Santos

"""

# carregando o banco de dados
 import pandas as pd

pnad = pd.read_csv('https://raw.githubusercontent.com/neylsoncrepalde/introducao_ao_python/master/pes_2012.csv')

# pedindo ajuda
help(pd.read_csv)

## lembrete [] delimita lista, {} dicionario e () tupla
## no phyton o missing value é NaN

pnad.shape # comando para olhar tamanho / dimensões (linhas e colunas)
pnad.columns # me dá os nomes das variáveis e o tipo de informação que vem
pnad.head # como no R mostra os primeiros casos
pnad['V8005'] # mostra a variável que eu quero 
pnad['V8005'].dtype # mostra o tipo de estrutura que ele é
pnad['V0302']
# ________________________________________________________________________

# estudando a variável idade
pnad['V8005'].describe() # estatísticas descritivas 
pnad['V8005'].describe().round(decimals=2) # arredonda valores
pnad['V8005'].mean() # média
pnad['V8005'].std() # desvio padrão
# ________________________________________________________________________

# estudando o banco
pnad.describe() # estatisticas das variáveis numpericas de todo o banco
pnad['V0302'].value_counts() # bom para tirar descritivas de variáveis categóricas

tab_sexo = pd.crosstab(index = pnad['V0302'], columns = ['count'])
print('Distribuição da Frequência Sexo'+'\n')
print(tab_sexo)

print('Porcentagens Sexo'+'\n')
(tab_sexo/tab_sexo.sum())*100 # tirando a média "manual"
# ________________________________________________________________________

# estudando a varável "cor / raça"
tab_cor = pnad['V0404'].value_counts()

print('Distribuição de Frequências'+'\n')
print(tab_cor)

print('Porcentagens Cor'+'\n')
print((tab_cor/tab_cor.sum())*100)

# cruzando sexo e cor
sexo_cor = pd.crosstab(index = pnad['V0404'], columns = pnad['V0302'])
print(sexo_cor)
# ________________________________________________________________________

### quando a ajuda do ctrl i não funciona usar: help(pd.Series.describe)


# estudando a variável renda 
pnad['V4720']


