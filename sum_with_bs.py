import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignoramos posibles errores con los certificados SSL.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Le paso el link de mi prueba.
url = input("Enter - ")

# Se hace la petición, se lee el documento y se parsea para entenderlo.
html = urllib.request.urlopen(url, context=ctx).read()
page = BeautifulSoup(html, 'html.parser')

# Creamos la lista con todos los tags de tipo 'span'
tags = page('span')

# Contar la suma de los número en el span.
count = 0
for tag in tags:
   # Revisamos el contenido del tag 'span', que es el número. Dado en formato de lista, para recuperar content[0]
    count += int(tag.contents[0])

# Impresión de la suma total.
print(count)