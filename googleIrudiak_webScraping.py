#-*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# REQUESTS --> deskargatutako HTML-a bueltatzen du, beraz irudiak falta dira (js-etik lortzen dira irudiak) --> emaitza ikusita honek ez du balio
# params:
#  q: bilaketa terminoa
#  tbm: google zerbitzua; adibidez isch --> google images
uri = "https://www.google.com/search?q=pinarello+f12&tbm=isch"
goiburuak = {'Host': 'www.google.com',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
erantzuna = requests.get(uri, headers=goiburuak, allow_redirects=False)
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)

# html-a lortu
html = erantzuna.content
file = open("google_img_search_results.html", "wb")
file.write(html)
file.close()

# SELENIUM + GEKODRIVER --> errendatutako HTML-a (nabigatzailea erabili behar da hau lortzeko)
# nabigatzailea ireki
browser = webdriver.Firefox()
# orrialdea ireki
browser.get(uri)
# esperar hasta que se haya renderizado el elemento que nos interesa (timeout=30s)
WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "rg_i.Q4LuWd")))
# HTML-a lortu
html = browser.page_source
# nabigatzailea itxi
browser.close()

# html-a parseatu
# soup DOM objektuaren erro elementuari erreferentzia egiten dio
soup = BeautifulSoup(html, 'html.parser')

# DOM zuhaitzean 'class' atributuaren  balioa "rg_i Q4LuWd" duten irudi guztiak bilatu
img_results = soup.find_all('img', {'class': 'rg_i Q4LuWd'})
for idx, each in enumerate(img_results):
    src = ""
    if each.has_attr('src'):
        src = each['src']
    else:
        src = each['data-src']
    print(str(idx) + " " + src)
