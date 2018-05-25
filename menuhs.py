import time
from colorama import Back, Style, Fore, init
init(autoreset=True)
opcion=0


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
	elif opcion==2:
		expansion="Journey to Un'Goro"
	elif opcion==3:
		expansion="Knights of the Frozen Throne"
	elif opcion==4:
		expansion="Kobolds & Catacombs"
	elif opcion==5:
		expansion="The Witchwood"
	elif opcion==6:
		exit
	else:
		print(Style.BRIGHT+Fore.YELLOW+"Opcion invalida")

