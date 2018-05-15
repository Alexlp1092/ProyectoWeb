import json
from pprint import pprint
import requests

print("¿Que quieres?")
print("Buscar una carta")
print("Buscar varias")
opcion=int(input("¿Que quieres?"))

if opcion==1:
  carta=input("Introduzca el nombre")
  response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/"+carta,
  headers={
    "X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA",
    "Accept": "application/json"
  }
)
  data=response.json()
  for carta in data:
    if carta["collectible"]==True:
      print("Nombre:",carta["name"])
      print("Vida:",carta["health"])
      print("Ataque:",carta["attack"])

else:
  print("Nada")



expansion="¿Que expansion deseas buscar?"

response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/"+expansion,
  headers={
    "X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA"
  }
)
data=response.json()

for carta in data:
	if carta["type"]=="Hero":
		print (carta["name"])
