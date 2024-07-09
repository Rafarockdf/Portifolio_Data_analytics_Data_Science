import pandas as pd
import geopandas as gpd
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

dados = pd.read_csv(r'dados.csv')
#lat_lon = pd.read_csv('lat_lon.csv')


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
#Função que transforma valores da coluna UF em nome dos estados respectivos. De acordo com a legenda fornecida nos dados pelo site kagle.
#A função foi criada para que seja possível obter a latitude e longitude dos estados a partir da biblioteca geopandas, para plotar um gráfico de mapa com a renda média por estado
def transcreve_estado_nome_completo(estado):
    if estado == 11:
        return 'Rondônia, Brasil'
    elif estado == 12:
        return 'Acre, Brasil'
    elif estado == 13:
        return 'Amazonas, Brasil'
    elif estado == 14:
        return 'Roraima, Brasil'
    elif estado == 15:
        return 'Pará, Brasil'
    elif estado == 16:
        return 'Amapá, Brasil'
    elif estado == 17:
        return 'Tocantins, Brasil'
    elif estado == 21:
        return 'Maranhão, Brasil'
    elif estado == 22:
        return 'Piauí, Brasil'
    elif estado == 23:
        return 'Ceará, Brasil'
    elif estado == 24:
        return 'Rio Grande do Norte, Brasil'
    elif estado == 25:
        return 'Paraíba, Brasil'
    elif estado == 26:
        return 'Pernambuco, Brasil'
    elif estado == 27:
        return 'Alagoas, Brasil'
    elif estado == 28:
        return 'Sergipe, Brasil'
    elif estado == 29:
        return 'Bahia, Brasil'
    elif estado == 31:
        return 'Minas Gerais, Brasil'
    elif estado == 32:
        return 'Espírito Santo, Brasil'
    elif estado == 33:
        return 'Rio de Janeiro, Brasil'
    elif estado == 35:
        return 'São Paulo, Brasil'
    elif estado == 41:
        return 'Paraná, Brasil'
    elif estado == 42:
        return 'Santa Catarina, Brasil'
    elif estado == 43:
        return 'Rio Grande do Sul, Brasil'
    elif estado == 50:
        return 'Mato Grosso do Sul, Brasil'
    elif estado == 51:
        return 'Mato Grosso, Brasil'
    elif estado == 52:
        return 'Goiás, Brasil'
    elif estado == 53:
        return 'Distrito Federal, Brasil'
    else:
        return 'Estado Desconhecido'
dados['Estado_completo'] = dados['UF'].apply(lambda x: transcreve_estado_nome_completo(x))
#Função quera latitude e longitude de cada estado e retorna as colunas necessárias.
def gera_latitude_longitude(df):
    gdf = gpd.tools.geocode(df['Estado_completo'], provider='nominatim', user_agent='my-application2', timeout=10)
    df['latitude'] = gdf.geometry.y
    df['longitude'] = gdf.geometry.x
    return df[['Estado','Estado_completo', 'latitude', 'longitude']]
#Criando uma tabela com os estados brasileiros sem repetição
estados = {}
estados['Estado_completo'] = dados['Estado_completo'].value_counts().keys()
estados['Estado'] = dados['Estado'].value_counts().keys()
estados = pd.DataFrame(estados)
lat_lon = gera_latitude_longitude(estados)
lat_lon.to_csv("lat_lon.csv")