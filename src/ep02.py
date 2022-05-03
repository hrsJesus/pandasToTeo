import pandas as pd
import numpy as np
import os

endereco_programa = os.path.join( os.path.abspath('.'), 'src' )
endereco_programa = os.path.dirname( os.path.abspath(__file__) )

endereco_projeto = os.path.dirname( endereco_programa )
endereco_dados = os.path.join( endereco_projeto, 'data')

filepath_csv = os.path.join( endereco_dados, 'tb_candidatura_2018.csv' )
df_candidatura = pd.read_csv( filepath_csv, sep=';' )

df_candidatura.head()

# Combinando e modificando colunas

df_candidatura.columns

df_candidatura[['idade_data_eleicao', 'idade_data_posse']]
tipos_colunas = df_candidatura[['idade_data_eleicao', 'idade_data_posse']].dtypes
type( tipos_colunas )
print( tipos_colunas )

idades_velhas = [ 'idade_data_eleicao', 'idade_data_posse' ]
idades_novas = [ 'idade_eleicao', 'idade_posse' ]

# Aqui dá pau!! Tem dado faltando
df_candidatura[idades_novas] = df_candidatura[idades_velhas].astype( int )
df_candidatura[idades_velhas].describe()

# Forma 1
del df_candidatura['idade_data_eleicao']

# Forma 2
df_candidatura_novo = df_candidatura.dropna( how='all', axis=1 ).copy() # Retorna dataframe novo
df_candidatura_novo.head()

df_candidatura_novo.columns

# Finalmente idade alterada
df_candidatura_novo['idade_data_posse'] = df_candidatura_novo['idade_data_posse'].astype( int )
df_candidatura_novo.dtypes

# Calculando o log da idade?
df_candidatura_novo['idade_data_posse_log'] = np.log( df_candidatura_novo['idade_data_posse'] )

# Vamos ver como ficou...
df_candidatura_novo[['idade_data_posse', 'idade_data_posse_log']].head()

# Inventando moda. Isso não faz sentido, ok?
df_candidatura_novo['campo_maluco'] = ( df_candidatura_novo['idade_data_posse'] + df_candidatura_novo['idade_data_posse_log'] ) * 2
df_candidatura_novo[['idade_data_posse', 'idade_data_posse_log', 'campo_maluco']].head()

# Vamos elaborar mais

def get_first_name(nome):
    return nome.lstrip(" ").split(" ")[0]

df_candidatura_novo['primeiro_nome'] = df_candidatura_novo['nome'].apply(get_first_name)
df_candidatura_novo[['nome', 'primeiro_nome']]

# Brincar com email

# df_candidatura_novo['email'].fillna('')
df_candidatura_novo['provedor'] = df_candidatura_novo['email'].fillna('').apply( lambda x: x.rstrip(" ").split('@')[-1])
