import urllib.request, urllib.error, urllib.parse

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

with open("romeo.txt", "w+") as text:
    data = fhand.read().decode()
    text.write(data)