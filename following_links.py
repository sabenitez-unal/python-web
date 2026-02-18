import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignoramos posibles errores con los certificados SSL.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Le paso el link de mi prueba.
url = input("Enter the URL: ")
# Posición
position = int(input("Enter the position: "))
# Veces
count = int(input("Enter the count: "))

for i in range(count+1):
    print(f"Retrieving: {url}")
    # Se hace la petición, se lee el documento y se parsea para entenderlo.
    if i < count:
        html = urllib.request.urlopen(url, context=ctx).read()
        page = BeautifulSoup(html, 'html.parser')
        tags = page("a")

        # Siguiente URL 
        url = tags[position-1].get("href", None)


name = tags[position-1].contents[0] # type: ignore
print(name)