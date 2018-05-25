import json
from pprint import pprint
import requests


expansion=input("Introduzca nombre de la expansion: ")

response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/"+expansion,
  headers={
    "X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA",
    "Accept": "application/json"
  }
)
data=response.json()

cartabusca=str(input("Introduzca el nombre de la carta que quieras buscar: "))
if cartabusca=="":
	for carta in data:
		if carta["type"]=="Hero" and 'collectible' in carta:
			print (carta["name"])
else:
	for carta in data:
		if carta["type"]=="Hero" and 'collectible' in carta and (carta["name"].startswith(cartabusca) or carta["name"].endswith(cartabusca)):
			print (carta["name"])
			print (carta["playerClass"])
			print (carta["text"])
		#Knights of the Frozen Throne