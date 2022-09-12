import srt as srt
from bs4 import BeautifulSoup
import requests

total_jornadas = 38
jornada = 1
#while jornada <= total_jornadas

print("https://www.comuniazo.com/comunio-apuestas/puntos?jornada=%s" % (jornada))

URL = "https://www.comuniazo.com/comunio-apuestas/puntos?jornada=%s" % (jornada)
req = requests.get(URL)
html = BeautifulSoup(req.text, "html.parser")

calendario = html.find_all('div', {'class': 'box box-match'})
#resultado = html.find_all('div', {'class': 'score'})
home = html.find_all('div', {'class': 'home'})
print(home)
for i, casa in enumerate(home):
    for href in casa.find_all('img class', src=True):
        casa = href.get('href')
        #print(casa)





