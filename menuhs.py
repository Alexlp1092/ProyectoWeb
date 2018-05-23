import time
opcion=0
while opcion!=6:
	print("Bienvenido a Searchstone")
	time.sleep(0.5)
	print("Elige una expansion del formato estandar o salir del programa: ")
	time.sleep(0.5)
	print("1) Clásica")
	time.sleep(0.2)
	print("2) Viaje a Un'Goro")
	time.sleep(0.2)
	print("3) Caballeros del Trono Helado")
	time.sleep(0.2)
	print("4) Kobolds y Catacumbas")
	time.sleep(0.2)
	print("5) El Bosque Embrujado")
	time.sleep(0.2)
	print("6) Salir")
	opcion=int(input("Introduzca opcion (1 al 6): "))
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
		print("Opcion invalida")
