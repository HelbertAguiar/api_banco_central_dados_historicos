import pandas as pd
from datetime import date


# Sistema Gerenciador de Séries Temporais do Bacen (SGS)
# https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries

# Endereço padrão da API:
# http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={dataInicial}&dataFinal={dataFinal}

# {codigo_serie} => codigo da serie a ser buscada, exemplo IPCA

def consulta_bc(codigo_serie, dataInicial='01/01/1900',  dataFinal=date.today().strftime('%d/%m/%Y')):  
    url = f'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={dataInicial}&dataFinal={dataFinal}'
    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df.set_index('data', inplace=True)
    return df


ipca = consulta_bc(433)
print(ipca)
print('\n', ''.rjust(30,'='))

ipca_mensal = consulta_bc(433, '01/01/2018', '31/12/2020')
print(ipca_mensal)
print('\n', ''.rjust(30,'='))

igpm = consulta_bc(433, '01/01/2018', '31/12/2020')
print(igpm)
print('\n', ''.rjust(30,'='))

selic_meta = consulta_bc(432)
print(selic_meta)
print('\n', ''.rjust(30,'='))

reservas_internacionais = consulta_bc(13621)
print(reservas_internacionais)
print('\n', ''.rjust(30,'='))

pnad = consulta_bc(24369)
print(pnad)
print('\n', ''.rjust(30,'='))

poupanca_pos_2012 = consulta_bc(195)
print(poupanca_pos_2012)
print('\n', ''.rjust(30,'='))

dolar = consulta_bc(1, '01/04/2021', '14/05/2021')
print(dolar)
print('\n', ''.rjust(30,'='))