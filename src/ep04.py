from curses import def_shell_mode
import pandas as pd
import os

pd.set_option('display.float_format', lambda x: '%.2f' % x)

endereco_programa = os.path.join( os.path.abspath('.'), 'src' )
endereco_programa = os.path.dirname( os.path.abspath(__file__) )

endereco_projeto = os.path.dirname( endereco_programa )
endereco_dados = os.path.join( endereco_projeto, 'data')

filepath_csv = os.path.join( endereco_dados, 'tb_candidatura_2018.csv' )
df_candidatura = pd.read_csv( filepath_csv, sep=';' )

# Objetivo: Encontrar a quantidade de deputados por estado, cor_raca, sexo, etc...

remove_columns = [ 'despesa_maxima_campanha', 'declara_bens', 'sigla_legenda', 'titulo_eleitoral', ]
keep_columns = list( set( df_candidatura.columns ) - set( remove_columns ) )

# Filtrando os candidatos a deputados estaduais
df_dept_estadual = df_candidatura[ (df_candidatura['descricao_cargo'] == 'DEPUTADO ESTADUAL') &
                                   (df_candidatura['descricao_situacao_candidatura'] == 'APTO') ][ keep_columns ]

# Percentual de aptos
df_dept_estadual.shape[0] / df_candidatura[ df_candidatura['descricao_cargo'] == 'DEPUTADO ESTADUAL'].shape[0]

df_dept_estadual.shape # Quantidade da nossa base...
df_dept_estadual['cpf'].nunique() # Sem duplicações


# Isso é um DataFrame, pois estamos usando [['cpf']], mas ele é multiIndex ('sigla_uf', 'descricao_genero')
agrupa_estado_genero = df_dept_estadual.groupby(['sigla_uf', 'descricao_genero'])[['cpf']].nunique()

# Desempilha os valores
df_estado_genero = agrupa_estado_genero.unstack()

# Remove multiIndex das colunas
df_estado_genero.columns = df_estado_genero.columns.droplevel()

# Reseta o índice do DataFrame
df_estado_genero = df_estado_genero.reset_index()

# Importando o pratrimônio dos colarinhos brancos...
filepath_xlsx = os.path.join( endereco_dados, 'tb_declaracao_2018.xlsx' )
df_patrimonio = pd.read_excel( filepath_xlsx )

# Agrupando para saber o patrimonio TOTAL dos camaradas...
df_patrimonio_candidato = df_patrimonio.groupby( ['numero_sequencial'] )[['valor']].sum().reset_index()

# Merge de patrimônio
df_full = pd.merge( df_candidatura,
                    df_patrimonio_candidato, 
                    how='left',
                    on=['numero_sequencial'])

# Descobrir partido com maior patrimonio medio entre os candidatos
df_filtrado = ( df_full[ df_full['descricao_situacao_candidatura'] == 'APTO' ]
                .sort_values( ['cpf', 'numero_turno'] )
                .drop_duplicates( 'cpf', keep='first')
                .fillna( {"valor": 0} ) )

# Descobringo os partidos mais "ricos"
df_partido = df_filtrado.groupby( ['sigla_partido'] ).agg( {"valor": ['sum', 'mean', 'median'] } )
df_partido.sort_values( [('valor', 'mean')], inplace=True )
print(df_partido)