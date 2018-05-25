import json
from pprint import pprint
import requests

expansion=input("Introduzca nombre de la carta: ")

response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/"+expansion+"?locale=esES",
  headers={
    "X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA"
  }
)
contador=0
data=response.json()
listamecanicas=[]

for carta in data:
	if 'collectible' in carta and 'mechanics' in carta:
		for mecanica in carta["mechanics"]:
			if mecanica["name"] not in listamecanicas:
				listamecanicas.append(mecanica["name"])

for mecanica in listamecanicas:
	print (mecanica)