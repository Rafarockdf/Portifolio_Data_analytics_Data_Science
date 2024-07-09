import pandas as pd
import geopandas as gpd
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.colors import sequential


dados = pd.read_csv(r'ProjetoDashPesquisaNacional-Python/dados.csv')
lat_lon = pd.read_csv('lat_lon.csv')

st.set_page_config(layout= 'wide')

def transcreve_estado(estado):
    if estado == 11:
        return 'RO'
    elif estado == 12:
        return 'AC'
    elif estado == 13:
        return 'AM'
    elif estado == 14:
        return 'RR'
    elif estado == 15:
        return 'PA'
    elif estado == 16:
        return 'AP'
    elif estado == 17:
        return 'TO'
    elif estado == 21:
        return 'MA'
    elif estado == 22:
        return 'PI'
    elif estado == 23:
        return 'CE'
    elif estado == 24:
        return 'RN'
    elif estado == 25:
        return 'PB'
    elif estado == 26:
        return 'PE'
    elif estado == 27:
        return 'AL'
    elif estado == 28:
        return 'SE'
    elif estado == 29:
        return 'BA'
    elif estado == 31:
        return 'MG'
    elif estado == 32:
        return 'ES'
    elif estado == 33:
        return 'RJ'
    elif estado == 35:
        return 'SP'
    elif estado == 41:
        return 'PR'
    elif estado == 42:
        return 'SC'
    elif estado == 43:
        return 'RS'
    elif estado == 50:
        return 'MS'
    elif estado == 51:
        return 'MT'
    elif estado == 52:
        return 'GO'
    elif estado == 53:
        return 'DF'
    else:
        return 'Estado Desconhecido'
dados['Estado'] = dados['UF'].apply(lambda x: transcreve_estado(x))
#Função que transforma valores da coluna UF em nome dos estados respectivos. De acordo com a legenda fornecida nos dados pelo site kagle.
#A função foi criada para que seja possível obter a latitude e longitude dos estados a partir da biblioteca geopandas, para plotar um gráfico de mapa com a renda média por estado
def transcreve_estado_nome_completo(estado):
    if estado == 11:
        return 'Rondônia'
    elif estado == 12:
        return 'Acre'
    elif estado == 13:
        return 'Amazonas'
    elif estado == 14:
        return 'Roraima'
    elif estado == 15:
        return 'Pará'
    elif estado == 16:
        return 'Amapá'
    elif estado == 17:
        return 'Tocantins'
    elif estado == 21:
        return 'Maranhão'
    elif estado == 22:
        return 'Piauí'
    elif estado == 23:
        return 'Ceará'
    elif estado == 24:
        return 'Rio Grande do Norte'
    elif estado == 25:
        return 'Paraíba'
    elif estado == 26:
        return 'Pernambuco'
    elif estado == 27:
        return 'Alagoas'
    elif estado == 28:
        return 'Sergipe'
    elif estado == 29:
        return 'Bahia'
    elif estado == 31:
        return 'Minas Gerais'
    elif estado == 32:
        return 'Espírito Santo'
    elif estado == 33:
        return 'Rio de Janeiro'
    elif estado == 35:
        return 'São Paulo'
    elif estado == 41:
        return 'Paraná'
    elif estado == 42:
        return 'Santa Catarina'
    elif estado == 43:
        return 'Rio Grande do Sul'
    elif estado == 50:
        return 'Mato Grosso do Sul'
    elif estado == 51:
        return 'Mato Grosso'
    elif estado == 52:
        return 'Goiás'
    elif estado == 53:
        return 'Distrito Federal'
    else:
        return 'Estado Desconhecido'
dados['Estado_completo'] = dados['UF'].apply(lambda x: transcreve_estado_nome_completo(x))
with st.sidebar:
    st.title('Filtros')
    
        
    option_estado = st.selectbox('Selecione um Estado',(
    "Brasil","AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
))
    option_sexo = st.selectbox('Filtre por Sexo',("Ambos","Maculino","Feminino"))
    
    if option_estado != "Brasil":
        mask_estado = dados['Estado'] == option_estado
        dados = dados[mask_estado]
    
    if option_sexo != 'Ambos' and option_sexo == 'Maculino':
        mask_sexo_m = dados['Sexo'] == 0
        dados = dados[mask_sexo_m]
    if option_sexo != 'Ambos' and option_sexo == 'Feminino':
        mask_sexo_f = dados['Sexo'] == 1
        dados = dados[mask_sexo_f]


renda_por_sexo = dados.groupby('Sexo')['Renda'].mean().reset_index()
renda_por_sexo['Sexo'] = renda_por_sexo['Sexo'].map({0: 'Masculino', 1: 'Feminino'})

renda_por_anos_estudo = dados.groupby('Anos de Estudo')['Renda'].mean().reset_index()



renda_por_estado = dados.groupby('Estado')['Renda'].mean().reset_index()
registros_por_estado = dados['Estado'].value_counts().reset_index()
renda_por_estado.columns = ['Estado', 'Renda']
registros_por_estado.columns = ['Estado', 'Frequência']
renda_por_estado_df = pd.merge(renda_por_estado, registros_por_estado, on='Estado')
renda_por_estado_df = pd.merge(renda_por_estado_df, lat_lon, on='Estado')


coluna_idade = 'Idade'
faixas_etarias = {
    'Grupo': ['18-24', '25-34', '35-44', '45-54', '55-64', '65+'],
    'Frequencia': [0, 0, 0, 0, 0, 0]
}
faixas_etarias = [18, 25, 35, 45, 55, 65, float('inf')]

# Criando as faixas etárias automaticamente
faixas_etarias_rotulos = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
dados['faixa_etaria'] = pd.cut(dados[coluna_idade], bins=faixas_etarias, labels=faixas_etarias_rotulos, right=False)

renda_por_faixa_etaria =  dados.groupby('faixa_etaria')['Renda'].mean().reset_index()


# CRIAÇÃO E CONFIGURAÇÃO DOS GRÁFICOS
fig_renda_por_sexo1 = px.bar(renda_por_sexo,
                             x = 'Sexo',
                             y = 'Renda',
                             text_auto = True,
                             title = 'Renda Média X Sexo')
fig_renda_por_sexo1.update_layout(yaxis_title = 'Renda Média')

fig_renda_por_sexo = px.pie(renda_por_sexo, values='Renda', names='Sexo', title='Renda Média X Sexo')




fig_renda_por_anos_estudo = px.line(renda_por_anos_estudo,
                                     x='Anos de Estudo',
                                     y='Renda',
                                     markers=True,  # Mostra marcadores
                                     title='Renda Média X Anos de Estudo')

# Personalizando o layout do gráfico
fig_renda_por_anos_estudo.update_layout(
    yaxis_title='Renda Média'  # Título do eixo y
)

fig_mapa_renda_media_por_estado = px.scatter_geo(renda_por_estado_df,
                                           lat='latitude',
                                           lon='longitude',
                                           scope='south america',
                                           size='Renda',
                                           template='seaborn',
                                           hover_name='Estado',
                                           hover_data={'latitude': False, 'longitude': False},
                                           title='Renda Média X Estado'
                                          )
# Tabela de frequência de faixa etária


fig_renda_por_faixa_etaria = px.histogram(renda_por_faixa_etaria, x="faixa_etaria",y='Renda',)
fig_renda_por_faixa_etaria.update_layout(
    title='Renda Média por Faixa Etária',
    xaxis_title='Faixa Etária',
    yaxis_title='Renda Média'
)




renda_media = dados['Renda'].mean()
media_anos_de_estudo = dados['Anos de Estudo'].mean()







# Começo do scopo do Dashboard

    


st.title(f'Dashboard Pesquisa Nacional')
# Análise dos Dados

    
col1, col2= st.columns(2)
with col1:
    st.metric('Renda Média',f'{renda_media:.2f}')
    st.plotly_chart(fig_mapa_renda_media_por_estado,use_container_width = True)
    st.plotly_chart(fig_renda_por_faixa_etaria,use_container_width = True)  
    
 
with col2:
    st.metric('Média Anos de Estudo',f'{media_anos_de_estudo:.0f}')
    st.plotly_chart(fig_renda_por_anos_estudo,use_container_width = True)
    st.plotly_chart(fig_renda_por_sexo, use_container_width=True)
    

