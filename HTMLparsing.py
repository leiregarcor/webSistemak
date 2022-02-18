#-*- coding: UTF-8 -*-

import requests
import sys
import urllib.parse
from bs4 import BeautifulSoup

# "bilatu" zerbitzuko imprimakiaren HTML kodean "<form" bilatu
# "method" atributuan datuak bidaltzeko erabili behar den metodoa adierazten da
metodoa = 'POST'
# "action" atributuan datuak jasoko dituen zerbitzariaren URI-a adieraztenda
uria = 'https://www.ehu.eus/bilatu/buscar/sbilatu.php?lang=es1'
goiburuak =  {'Host': 'www.ehu.eus',
             'Content-Type': 'application/x-www-form-urlencoded'}
# bidaliko den balioaren parametroaren izena
# dagokion "<input" elementuaren "name" atributuan adierazten da
edukia = {'abi_ize': sys.argv[1]}
# datuak inprimaki formatuan kodifikatu
edukia_encoded = urllib.parse.urlencode(edukia)
goiburuak['Content-Length'] = str(len(edukia_encoded))
# orain "buscar" botoia sakatzen dugula emulatzen dugu
# hots, HTTP eskaera bidaltzen du
erantzuna = requests.request(metodoa, uria, headers=goiburuak, data=edukia_encoded, allow_redirects=False)

# HTTP erantzunak:
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
html = erantzuna.content
#print(html)

# bilaketaren emaitzak dituen HTML kodea parseatuko dugu
soup = BeautifulSoup(html,'html.parser')
errenkadak = soup.find_all('td', {'class': 'fondo_listado'}) # array motakoa izango da
for idx, errenkadak in enumerate(errenkadak):
    izen_bizenak = errenkadak.a.text
    esteka = "https://www.ehu.eus" + errenkadak.a['href']
    print(str(idx) + "-" + izen_bizenak + ": " + esteka)


