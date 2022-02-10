import requests

# HELBURUA: web bezero honek irdudi bat deskargatuko du

# HTTP eskaerak 4 eremu ditu:
metodoa = "GET"
uria = "http://www.httpwatch.com/httpgallery/chunked/chunkedimage.aspx"
goiburuak = {'Host':'www.httpwatch.com'}
edukia = ""

# eskaera bidali eta erantzuna jaso (guztia parametrizatuta dago)
erantzuna = requests.request(metodoa, uria, headers=goiburuak, data=edukia)

# HTTP erantzunak 4 eremu ditu:
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
for goiburua in erantzuna.headers:  # erantzuna.headers hiztegi bat da
    print(goiburua + ": " + erantzuna.headers[goiburua])
edukia = erantzuna.content
print(edukia)

fitxategia = open("irudia.jpg", "wb")
fitxategia.write(edukia)
fitxategia.close()