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
for carta in data:
	if 'rarity' in carta and carta["rarity"]=="Legendary" and 'collectible' in carta:
		print(carta["name"])
		contador=contador+1
print("En esta expansion hay ",contador,"cartas legendarias")