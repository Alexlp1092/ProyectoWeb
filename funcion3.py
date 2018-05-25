expansion=input("Introduzca nombre de la carta: ")

response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/"+expansion+"?locale=esES",
  headers={
    "X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA"
  }
)
contador=0
data=response.json()
parametro="a"
while parametro!="ATK" and parametro!="MAN" and parametro!="HLT":
	parametro=input("¿Por que parametro quieres filtrar? ATK/MAN/HLT: ")
	if parametro!="ATK" and parametro!="MAN" and parametro!="HLT":
		print("Parametro invalido")
if parametro=="ATK":
	parametro="attack" 
elif parametro=="MAN":
	parametro="cost" 
elif parametro=="HLT":
	parametro="health" 

vaparametro=int(input("Introduzca el valor del parametro: "))
for carta in data:
	if 'collectible' in carta and parametro in carta and carta[parametro]==vaparametro:
		if carta["playerClass"]=="Warrior":
			print(Fore.RED+carta["name"])
		elif carta["playerClass"]=="Shaman":
			print(Fore.BLUE+carta["name"])
		elif carta["playerClass"]=="Rogue":
			print(Fore.BLACK+carta["name"])
		elif carta["playerClass"]=="Paladin":
			print(Fore.YELLOW+carta["name"])
		elif carta["playerClass"]=="Hunter":
			print(Fore.GREEN+carta["name"])
		elif carta["playerClass"]=="Druid":
			print("\033[32;33;40m"+carta["name"])
		elif carta["playerClass"]=="Warlock":
			print(Fore.MAGENTA+carta["name"])
		elif carta["playerClass"]=="Mage":
			print(Fore.CYAN+carta["name"])
		else:
			print(carta["name"])
		contador=contador+1
print("En esta expansion hay",contador,"cartas con este valor")
