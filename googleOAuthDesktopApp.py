import requests
import urllib
import webbrowser
import socket
import json

# https://developers.google.com/identity/protocols/oauth2/native-app
print("###################################")
print("OAuth 2.0 for Mobile & Desktop Apps")
print("###################################")

print("\nPrerequisites on Google Cloud Console")
print("\tEnable APIs for your project")
print("\tIdentify access scopes")
# see and download all your Google Drive files
scope = "https://www.googleapis.com/auth/drive.readonly"
print("\tCreate authorization credentials")
client_id = "682238149092-q0ang5o5scav8vqq6ahg0pu5a8tn4ghs.apps.googleusercontent.com"
client_secret = "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" # gako sekretu hau enkriptatuta egon beharko luke eta beste fitxategi batean seguratsauna bermatzeko
print("\tConfigure OAuth consent screen")
print("\t\tAdd access scopes and test users")

print("\nObtaining OAuth 2.0 access tokens")

print("\tStep 2: Send a request to Google's OAuth 2.0 server")
base_uri = "https://accounts.google.com/o/oauth2/v2/auth"
goiburuak = {'Host': 'accounts.google.com',
             'User-Agent': 'OAuth WebAPIs demonstrator'}
datuak = {'client_id': client_id,
          'redirect_uri': 'http://127.0.0.1:8090', # Dirección IP de bucle invertido
          'response_type': 'code',
          'scope': scope,}
datuak_kodifikatuta = urllib.parse.urlencode(datuak) # parametroak URI-an daude
step2_uri = base_uri + '?' + datuak_kodifikatuta
print("\t" + step2_uri)
webbrowser.open_new(step2_uri)
print("\n\tStep 3: Google prompts user for consent")

print("\n\tStep 4: Handle the OAuth 2.0 server response")
# 8090. portuan entzuten dagoen zerbitzaria sortu
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind(('localhost', 8090))
listen_socket.listen(1)
print("\t\tSocket listening on port 8090")

# nabitzailetik 302 eskaera jaso
# ondorengo lerroan programa gelditzen da zerbitzariak 302 eskaera jasotzen duen arte
client_connection, client_address = listen_socket.accept()
eskaera = client_connection.recv(1024).decode()
print("\t\tNabigatzailetik ondorengo eskaera jaso da:")
print("\n" + eskaera) # zerbitzariak jasotzen duen eskaera

# eskaeran "auth_code"-a bilatu
lehenengo_lerroa = eskaera.split('\n')[0]
aux_auth_code = lehenengo_lerroa.split(' ')[1]
auth_code = aux_auth_code[7:].split('&')[0]
print("auth_code: " + auth_code)

# erabiltzaileari erantzun bat bueltatu
http_response = """\
HTTP/1.1 200 OK

<html>
<head><title>Proba</title></head>
<body>
The authentication flow has completed. Close this window.
</body>
</html>
"""
client_connection.sendall(str.encode(http_response))
client_connection.close()

print("\n\tStep 5: Exchange authorization code for refresh and access tokens")
uri = 'https://oauth2.googleapis.com/token'
goiburuak = {'Host': 'oauth2.googleapis.com',
             'Content-Type': 'application/x-www-form-urlencoded'}
datuak = {'client_id': client_id,
          'client_secret': client_secret,
          'code': auth_code,
          'grant_type': 'authorization_code',
          'redirect_uri': 'http://127.0.0.1:8090',}
datuak_kodifikatuta = urllib.parse.urlencode(datuak)
goiburuak['Content-Length'] = str(len(datuak_kodifikatuta))
erantzuna = requests.post(uri, headers=goiburuak, data=datuak_kodifikatuta, allow_redirects=False) # eskaera ez dugu nabigatzaileanegingo, gure programan egingo da
status = erantzuna.status_code
print("\t\tStatus: " + str(status))

# Google responds to this request by returning a JSON object
# that contains a short-lived access token and a refresh token.
edukia = erantzuna.text
print("\t\tEdukia:")
print("\n" + edukia)
edukia_json = json.loads(edukia)
access_token = edukia_json['access_token']
print("\naccess_token: " + access_token)
print("The authentication flow has completed.")

print("\nCalling Google APIs")
# Drive API --> Files --> list
# https://developers.google.com/drive/api/v3/reference/files/list
uri = 'https://www.googleapis.com/drive/v3/files'
goiburuak = {'Host': 'www.googleapis.com',
             'Authorization': 'Bearer ' + access_token}
erantzuna = requests.get(uri, headers=goiburuak, allow_redirects=False)
status = erantzuna.status_code
print("\tStatus: " + str(status))
edukia = erantzuna.text
print("\tEdukia:")
print(edukia)
print("Press enter to process JSON data structure...")
edukia_json = json.loads(edukia)
for each in edukia_json['files']:
    print(each['name'])
