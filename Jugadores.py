import pandas as pd
import requests
import numpy as np

url = "https://www.comuniazo.com/comunio-apuestas/jugadores/"

r = requests.get(url)
df_list = pd.read_html(r.text)

#print(df_list[0].values)

values = []
for el in df_list[0].values:
    aux = []
    for i in el:
        aux.append(i)
    values.append(aux)

#f = open("Jugadores.txt", 'a+')
f = open('Jugadores.txt', 'w')
f.write("Clasificación,Equipo,Puntos,PJ,PG,PE,PP,GF,GC,DF")
f.write('\n')

for el in values:
    stringer = ''
    for i in el:
        stringer += str(i)+','
    stringer = stringer[:-1]
    f.write(stringer)
    f.write('\n')

f.close()



