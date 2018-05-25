import json
from pprint import pprint
import requests
from colorama import Back, Style, Fore, init
init(autoreset=True)

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
		print(Style.BRIGHT+"Nombre:", carta["name"])

		print(Style.BRIGHT+"Tipo:", carta["type"])

		if carta["rarity"]=="Common":
			print(Style.BRIGHT+"Rareza:", carta["rarity"])
		elif carta["rarity"]=="Rare":
			print(Style.BRIGHT+"Rareza:",Fore.BLUE+carta["rarity"])
		elif carta["rarity"]=="Epic":
			print(Style.BRIGHT+"Rareza:",Fore.MAGENTA+carta["rarity"])		
		elif carta["rarity"]=="Legendary":
			print(Style.BRIGHT+"Rareza:",Fore.YELLOW+carta["rarity"])	

		print(Style.BRIGHT+"Coste:",Fore.CYAN+str(carta["cost"]))

		if 'attack' in carta:
			print(Style.BRIGHT+"Ataque:",Fore.YELLOW+str(carta["attack"]))

		if 'health' in carta:
			print(Style.BRIGHT+"Vida:",Fore.RED+str(carta["health"]))

		if carta["playerClass"]=="Warrior":
			print(Style.BRIGHT+"Clase:",Fore.RED+carta["playerClass"])
		elif carta["playerClass"]=="Shaman":
			print(Style.BRIGHT+"Clase:",Fore.BLUE+carta["playerClass"])
		elif carta["playerClass"]=="Rogue":
			print(Style.BRIGHT+"Clase:",Fore.BLACK+carta["playerClass"])
		elif carta["playerClass"]=="Paladin":
			print(Style.BRIGHT+"Clase:",Fore.YELLOW+carta["playerClass"])
		elif carta["playerClass"]=="Hunter":
			print(Style.BRIGHT+"Clase:",Fore.GREEN+carta["playerClass"])
		elif carta["playerClass"]=="Druid":
			print(Style.BRIGHT+"Clase:",Fore.BROWN+carta["playerClass"])
		elif carta["playerClass"]=="Warlock":
			print(Style.BRIGHT+"Clase:",Fore.MAGENTA+carta["playerClass"])
		elif carta["playerClass"]=="Mage":
			print(Style.BRIGHT+"Clase:",Fore.CYAN+carta["playerClass"])
		else:
			print(Style.BRIGHT+"Clase:",carta["playerClass"])

		if 'text' in carta:
			print(Style.BRIGHT+"Descripcion:", carta["text"])
