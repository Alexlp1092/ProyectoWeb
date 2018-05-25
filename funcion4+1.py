import json
from pprint import pprint
import requests
from colorama import Back, Style, Fore, init
init(autoreset=True)

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
			print (carta["text"])
