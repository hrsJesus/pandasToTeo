import pandas as pd

# Series
serie_receita = pd.Series( data=[1, 4, 10, 2, 1000000, 200, None], name='receita' )

# Mostrando a serie criada
print( "Nossa série: ", serie_receita )
print( "Tipo da nossa série: ", type( serie_receita ) )

# DataFrame

dados = { "nome": ['Teo', 'Nah', 'Code', 'Karlla'],
          "sobrenome": ['Calvo', 'Ataide', 'Show', 'Mag'],
          "idade": [28, 30, 32, 30] }

df = pd.DataFrame( data=dados )

# Comçando a aula...

# Lendo um csv...
pathfile_csv = '/home/hrsjesus/repos/TMW/pandas/PandasToTeo/data/tb_candidatura_2018.csv'
df_candidatura = pd.read_csv(pathfile, sep=";")
df_candidatura.head()

# lendo um xlsx
pathfile_xlsx = '/home/hrsjesus/repos/TMW/pandas/PandasToTeo/data/tb_declaracao_2018.xlsx'
df_declaracao = pd.read_excel( pathfile_xlsx)
df_declaracao.head()

############################
# Brincando com o DataFrame
############################

# Número de linhas para serem exibidas a partir da primeira
df_candidatura.head(2) # Isso é um método

# Número de linhas para serem exibidas a partir da última
df_candidatura.tail(2) # Isso é um método

# Número de linhas e colunas de um dataframe (tupla)
df_candidatura.shape[0] # Isso é um atributo

# Quais são as colunas do Dataframe? Sabemos que temos 45 colunas
df_candidatura.columns # Outro atributo

# Navegando pelas colunas do DataFrame...
df_candidatura['nome'] # Retorna séries com o nome, ou coluna, melhor dizendo

df_candidatura[['nome', 'cpf']]

df_candidatura[['nome', 'cpf', 'descricao_ocupacao']]

# Navegando pelas colunas e linhas do DataFrame...
df_candidatura['nome'][29140] # df[column][index]

# Informações do DataFrame...
df_candidatura.info()

# Navegando apenas nas linhas
df_candidatura.iloc[29140:29145]

# quantas linhas, colunas tem a base de declaracao
