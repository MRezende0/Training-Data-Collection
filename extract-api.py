import requests
from bs4 import BeautifulSoup as bs

chave_api = '2DNNA7ZKLPUHQSSN'

url = 'https://economia.awesomeapi.com.br/USD-BRL/10?start_date=20200201&end_date=20230229'
r = requests.get(url)
data = r.json()

print(data)