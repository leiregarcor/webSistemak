import requests

# HELBURUA: web bezero hau egelako orrialde nagusira konektatuko da

# HTTP eskaerak 4 eremu ditu:
metodoa = "GET"
uria = "http://egela.ehu.eus/"
goiburuak = {'Host': 'egela.ehu.eus'}
edukia = ""

# eskaera bidali (eskaeraren metodoa liburutegiaren metodoan adierazi eta erantzuna jaso)
erantzuna = requests.get(uria, headers=goiburuak, data=edukia, allow_redirects=False)

# HTTP erantzunak 4 eremu ditu:
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
location = erantzuna.headers['Location']
print("Location: " + location)

#honaino egindako kodea exekutatu ondoren:
# 302 Found status eta deskribapena lortzen ditugu -> berbideraketa egin behar da

##### Eskaera berria 'Location' goiburuak adierazten duen URI-a
# HTTP eskaerak 4 eremu ditu:
metodoa = "GET"
uria = location
goiburuak = {'Host': uria.split('/')[2]}
edukia = ""

# eskaera bidali (eskaeraren metodoa liburutegiaren metodoan adierazi eta erantzuna jaso)
erantzuna = requests.get(uria, headers=goiburuak, data=edukia, allow_redirects=False)

# HTTP erantzunak 4 eremu ditu:
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
location = erantzuna.headers['Location']
print("Location: " + location)
#honaino egindako kodea exekutatu ondoren:
#303 See Other status eta deskribapena lortzen ditugu -> berbideraketa egin behar da
