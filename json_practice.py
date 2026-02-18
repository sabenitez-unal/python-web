import urllib.request
import json

url = input("Dame la URL: ")

print(f"Retrieving {url}...")

request = urllib.request.urlopen(url)
response = request.read()

data = json.loads(response)

count = 0
for comment in data["comments"]:
    count += comment["count"]

print(f"Count: {count}")