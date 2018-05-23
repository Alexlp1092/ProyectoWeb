import json
from pprint import pprint
import requests

expansion=input("Introduzca nombre de la carta: ")

response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/"+expansion+"?locale=esES",
  headers={
    "X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA"
  }
)
data=response.json()
nombre=input("Introduzca nombre de la carta: ")

for carta in data:
	if 'collectible' in carta and carta["name"]==nombre:
		print("Nombre:", carta["name"])
		print("Tipo:", carta["type"])
		print("Rareza:", carta["rarity"])
		print("Coste:", carta["cost"])
		print("Ataque:", carta["attack"])
		print("Vida:", carta["health"])
		print("Descripcion:", carta["text"])