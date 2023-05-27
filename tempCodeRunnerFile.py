import requests

res = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacoes = res.json()

cotacoes['USDBRL']['bid']