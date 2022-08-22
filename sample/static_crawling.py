import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.naver.com'
reponse = requests.get(url)
html_text = reponse.text

html = bs(html_text, 'html.parser')