import requests
from bs4 import BeautifulSoup as bs

api_key = 'mhJGQjLs0V6pBBn0OCT3npKenZTDHDO6'

url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.10844/dados'

r = requests.get(url)
data = r.json()

print(data)