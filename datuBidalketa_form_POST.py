import urllib.parse
import requests

# HELBURUA: NAN zenbakiaren letra kalkulatzeko
# nabigatzaileak egiten duena simulatuko dugu

uria = "http://ws-sendingformdata.appspot.com/processForm"
goiburuak = {'Host': 'ws-sendingformdata.appspot.com',
             'Content-Type': 'application/x-www-form-urlencoded'}

# datuak hiztegi batean adieraziko ditut
edukia = {'nan': '16102927'}
# datuak imprimaki formatuan duen kate batean bihurtuko ditut
# zelan? urllib liburutegia erabiliz
edukia_encoded = urllib.parse.urlencode(edukia)
goiburuak['Content-Length'] = str(len(edukia_encoded))
erantzuna = requests.post(uria, headers=goiburuak, data=edukia_encoded, allow_redirects=False)

# HTTP erantzunak:
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
edukia = erantzuna.content
print(edukia)
