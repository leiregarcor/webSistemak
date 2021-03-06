import requests
import sys
import zlib

# HELBURUA:

# HTTP eskaerak:
uria = "https://www.google.es/"
goiburuak = {'Host':'www.google.es'}

compressed = False
if len(sys.argv) == 1:
    #parametrorik gabe exekutatzean bigarren goiburu hau gehitzen da eta edukia ez da konprimatzen
    goiburuak['Accept-Encoding']= 'identity'
elif sys.argv[1] == 'compress':
    compressed = True
    goiburuak['Accept-Encoding'] = 'gzip'
else:
    print("Errorea! Erabilera: pyhton compression.py compress")
    exit(0)

# eskaera bidali (eskaeraren metodoa liburutegiaren metodoan adierazi eta erantzuna jaso)
erantzuna = requests.get(uria, headers=goiburuak, allow_redirects=False, stream=True)

# HTTP erantzunak:
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)

# erantzunak edukia modu gordinean atera:
print("RESPONSE CONTENT LENGTH: " + str(len(erantzuna.raw.data)) + " byte")
if compressed:
    edukia_compressed = erantzuna.raw.data
    print(edukia_compressed)
    edukia_uncompressed = zlib.decompress(edukia_compressed, 16 + zlib.MAX_WBITS)
    print(edukia_uncompressed)
    print("UNCOMPRESSED RESPONSE CONTENT LENGTH: " + str(len(edukia_uncompressed)) + " byte")