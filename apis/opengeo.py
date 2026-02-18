import urllib.request, urllib.parse
import json, ssl

serviceurl = "https://py4e-data.dr-chuck.net/opengeo?"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Dame la ubicación: ")
    if len(address) < 1: break

    address = address.strip()
    params = dict()
    params['q'] = address

    url = serviceurl + urllib.parse.urlencode(params)

    print(f'Retrieving {url}')

    response = urllib.request.urlopen(url, context=ctx)
    data = response.read().decode()

    print(f"Retrieved {len(data)}, characters {data[:20].replace('\n', ' ')}")

    try: 
        js = json.loads(data)
    except:
        print(f"Problemitas con el servidor. D: {Exception}")
        print("")
        break

    if "features" not in js:
        print("Error de descarga... ")
        break
    elif len(js["features"]) == 0:
        print("No encontrado. :(")
        break

    with open("apis/location.json", "w") as document:
        json.dump(js, document, indent=4)

    plus_code = js["features"][0]["properties"]["plus_code"]
    print(f"The Plus Code of the location is {plus_code}")