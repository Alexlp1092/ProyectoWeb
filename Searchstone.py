import time
from colorama import Back, Style, Fore, init
import requests
init(autoreset=True)
opcion=0


def menu2(data, opcion):
	#comienzo funcion1
	def opcion1(data):
		nombre=input(Style.BRIGHT+Fore.YELLOW+"Introduzca nombre de la carta: ")
		print()
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
		print()

	#COMIENZO FUNCION2
	def opcion2(data):
		contador=0
		for carta in data:
			if 'rarity' in carta and carta["rarity"]=="Legendary" and 'collectible' in carta:
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
		print()
		print("En esta expansion hay ",contador,"cartas legendarias")
		print()



	def opcion3(data):
		contador=0
		parametro="a"
		print()
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
		print()
		print("En esta expansion hay",contador,"cartas con este valor")
		print()

	def opcion4(data):
		contador=0
		listamecanicas=[]
		for carta in data:
			if 'collectible' in carta and 'mechanics' in carta:
				for mecanica in carta["mechanics"]:
					if mecanica["name"] not in listamecanicas:
						listamecanicas.append(mecanica["name"])
		print()
		for mecanica in listamecanicas:
			print (mecanica)
		print()


	def opcion5(data,opcion):
		if opcion==3:
			cartabusca=str(input("Introduzca el nombre de la carta que quieras buscar: "))
			print()
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
		else:
			print("En esta expansion no hay cartas de heroe")
		print()


	nopcion=0
	while nopcion!=6:
		print(Style.BRIGHT+Fore.YELLOW+"1) Informar sobre una carta de la expansion")
		print(Style.BRIGHT+Fore.YELLOW+"2) Contar cuantas legendarias hay en la expansion")
		print(Style.BRIGHT+Fore.YELLOW+"3) Buscar por parametro (Ataque, Coste de maná o Vida)")
		print(Style.BRIGHT+Fore.YELLOW+"4) Listar las mecanicas que hay en la expansion")
		print(Style.BRIGHT+Fore.YELLOW+"5) Informacion sobre carta de Heroe (solo disponible en Caballeros del Trono Helado)")
		print(Style.BRIGHT+Fore.YELLOW+"6) Salir")
		nopcion=int(input(Style.BRIGHT+Fore.YELLOW+"Introduzca opcion (1 al 6): "))
		if nopcion==1:
			opcion1(data)
		elif nopcion==2:
			opcion2(data)
		elif nopcion==3:
			opcion3(data)
		elif nopcion==4:
			opcion4(data)
		elif nopcion==5:
			opcion5(data,opcion)
		elif nopcion==6:
			exit
		else:
			print(Style.BRIGHT+Fore.YELLOW+"Opcion invalida")


while opcion!=6:
	print(Style.BRIGHT+Fore.YELLOW+"Bienvenido a Searchstone")
	time.sleep(0.5)
	print(Style.BRIGHT+Fore.YELLOW+"Elige una expansion del formato estandar o salir del programa: ")
	time.sleep(0.5)
	print(Style.BRIGHT+Fore.YELLOW+"1) Clásica")
	time.sleep(0.2)
	print(Style.BRIGHT+Fore.GREEN+"2) Viaje a Un'Goro")
	time.sleep(0.2)
	print(Style.BRIGHT+Fore.CYAN+"3) Caballeros del Trono Helado")
	time.sleep(0.2)
	print(Style.BRIGHT+Fore.RED+"4) Kobolds y Catacumbas")
	time.sleep(0.2)
	print(Style.BRIGHT+Fore.BLUE+"5) El Bosque Embrujado")
	time.sleep(0.2)
	print(Style.BRIGHT+Fore.YELLOW+"6) Salir")
	opcion=int(input(Style.BRIGHT+Fore.YELLOW+"Introduzca opcion (1 al 6): "))
	print(opcion)
	if opcion==1:
		expansion="Classic"
		response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/"+expansion+"?locale=esES",headers={
			"X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA"})
		data=response.json()
		menu2(data, opcion)
	elif opcion==2:
		expansion="Journey to Un'Goro"
		response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/"+expansion+"?locale=esES",headers={
			"X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA"})
		data=response.json()
		menu2(data, opcion)
	elif opcion==3:
		expansion="Knights of the Frozen Throne"
		response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/"+expansion+"?locale=esES",headers={
			"X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA"})
		data=response.json()
		menu2(data, opcion)
	elif opcion==4:
		expansion="Kobolds & Catacombs"
		response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/"+expansion+"?locale=esES",headers={
			"X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA"})
		data=response.json()
		menu2(data, opcion)
	elif opcion==5:
		expansion="The Witchwood"
		response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/"+expansion+"?locale=esES",headers={
			"X-Mashape-Key": "RdEHCET0tBmshzcVxojLE997hAvNp1qWbaQjsn2UdJz0ad4JQA"})
		data=response.json()
		menu2(data, opcion)
	elif opcion==6:
		exit
	else:
		print(Style.BRIGHT+Fore.YELLOW+"Opcion invalida")