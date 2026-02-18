import requests
import re

url = input("Enter de URL: ")

response = requests.get(url)

with open("text-with-numbers.txt", "w+") as text:
    text.write(response.text)
    text.seek(0)
    txt = text.read()

numbers_list = re.findall("[0-9]+", txt)

count = 0
for number in numbers_list:
    count += int(number)

print(f"The sum result: {count}")
