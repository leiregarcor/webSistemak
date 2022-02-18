import urllib.parse
import requests

# HELBURUA: NAN zenbakiaren letra kalkulatzeko
# nabigatzaileak egiten duena simulatuko dugu

uria = "http://ws-sendingformdata.appspot.com/processForm"
goiburuak = {'Host': 'ws-sendingformdata.appspot.com'}
edukia = {'nan': '16102927'} # datuak hiztegi batean adieraziko ditut
# edukia URI-an bertan doa
edukia_encoded = urllib.parse.urlencode(edukia) #histegi bat ezin da sartu URI-an -> urllib era aproposean jartzen du
uria = uria + '?' + edukia_encoded
erantzuna = requests.get(uria, headers=goiburuak, allow_redirects=False)

# HTTP erantzunak:
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)

edukia = erantzuna.content
print(edukia)
