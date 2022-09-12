from bs4 import BeautifulSoup
import requests

URL = "https://www.comuniazo.com/comunio-apuestas/jugadores/"
req = requests.get(URL)
html = BeautifulSoup(req.text, "html.parser")

dictionary = {}
lEquipos = []
lImg = []

equipos = html.find_all('div', {'class': 'filter-teams'})


for i, equipo in enumerate(equipos):
    for href in equipo.find_all('a',href=True):
        team = href.get('href').replace('https://www.comuniazo.com/comunio-apuestas/equipos/', '').replace('-', ' ').title()
        lEquipos.append(team)

    for src in equipo.find_all('img'):
        lImg.append(src.get('src'))

    contador = 0
    for el in lEquipos:
        dictionary[el] = lImg[contador]
        contador+=1

#print(dictionary)
f = open('Equipos.txt', 'w')
f.write("Equipo,Escudo")
f.write('\n')

for el in dictionary:
    f.write(el+  ','+ dictionary[el] + '\n')

f.close()