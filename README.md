# api_banco_central_dados_historicos
Uso da API Banco Central para buscar alguns indices, por exemplo: IPCA e SELIC.

## Sistema Gerenciador de Séries Temporais do Bacen (SGS)
https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries

## Endereço padrão da API:
http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={dataInicial}&dataFinal={dataFinal}
