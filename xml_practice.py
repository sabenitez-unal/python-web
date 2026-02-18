import xml.etree.ElementTree as et
import urllib.request

url = input("Give me the URL: ")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_2370453.xml"

print(f"Retrieving {url}")

xml_document = urllib.request.urlopen(url).read()

print(f"Retrieved {len(xml_document)} characters")

xml = et.fromstring(xml_document)
counts = xml.findall(".//count")

suma = 0
for count in counts:
    suma += int(count.text) # type: ignore

print(f"Result: {suma}")
