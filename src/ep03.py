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

### Aula de hoje é sobre limpeza e filtros de dados

# Idenficando o % de missings em cada coluna
df_candidatura.isna().sum() / df_candidatura.shape[0]

# Removendo colunas com apenas missings (NaNs)
# df_candidatura = df_candidatura.dropna( how='all', axis=1 )
df_candidatura.dropna( how='all', axis=1, inplace=True )

# Removendo candidatos que não tem email ou composição legenda
df_candidatura.dropna( axis=0,
                       how='any',
                       subset=['composicao_legenda', 'email'],
                       inplace=True )

# Vamos filtrar
df_candidatura['descricao_cargo'].unique()

df_candidatura['descricao_cargo'].nunique()

df_presidente_pstu = df_candidatura[ (df_candidatura['descricao_cargo'] == 'PRESIDENTE') &
                                (df_candidatura['sigla_partido'] == 'PSTU') ]

# Pegando todos os candidatos à presidência
df_presidente = df_candidatura[ (df_candidatura['descricao_cargo'] == 'PRESIDENTE') ].copy()

colunas_interesse = ['ano_eleicao',
                     'numero_turno',
                     'cpf',
                     'data_nascimento',
                     'descricao_cor_raca',
                     'descricao_estado_civil',
                     'descricao_genero',
                     'descricao_grau_instrucao',
                     'descricao_ocupacao',
                     'email',
                     'nome',
                     'nome_social',
                     'sigla_uf_nascimento',
                     'nome_partido',
                     'sigla_partido',
                     'descricao_cargo',
                     'descricao_situacao_candidatura']

df_presidente = df_presidente[colunas_interesse]

# Quantos candidato a presidente temos?
df_presidente.shape # 16

# Tem boi na linha amiguinhooo
df_presidente['cpf'].nunique()

df_presidente = ( df_presidente
                  .sort_values(by=['cpf', 'numero_turno'])
                  .drop_duplicates( subset=['cpf'], keep='first' ) )

df_presidente.where( df_presidente['descricao_situacao_candidatura'] == "APTO" ).dropna(how='all') # Faz o mesmo que a linha de baixo (só que transforma os int em float)
df_presidente = df_presidente[ df_presidente['descricao_situacao_candidatura'] == "APTO" ].copy() # Faz o mesmo que alinha de cima
