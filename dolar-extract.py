import requests
from bs4 import BeautifulSoup as bs

url = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-dolar')
soup = bs(url.text, 'html.parser')

dolar = soup.find('div', {'class': 'style__Text-sc-1a6mtr6-2 ljisZu'}).text[0:4]
dolar = dolar.replace(',', '.')
dolar = float(dolar)

print(dolar)