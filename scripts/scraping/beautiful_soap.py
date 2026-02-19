import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Para ignorar errores del certificado SSL de las páginas.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("URL: ")
cont = input("")
html = urllib.request.urlopen(url, context=ctx).read()
soap = BeautifulSoup(html, 'html.parser')

tags = soap(cont)
for tag in tags:
    print(tag.contents)