#1. Listar tipos de documentos adjuntos

def Tiposadjuntos(datos):
	lista=[]
	listaadjuntos=[]
	listatipos=[]
	for documento in datos["expediente"]["anuncios"]["anuncio"]:
		lista.append(documento)
	for elem in lista:
		if type(elem["documentoAdjunto"]) == list:
			for elem2 in elem["documentoAdjunto"]:
				listatipos.append(elem2["tipo"])
		elif type(elem["documentoAdjunto"])==dict:
			listatipos.append(elem["tipo"])
	return listatipos


#2. Pedir por teclado el tipo de anuncio y cuenta los anuncios relacionados

def contarrelacionados(cad,datos):
	listarelacionados=[]
	for documento in datos["expediente"]["anuncios"]["anuncio"]:
		if documento["tipoContrato"]==cad:
			for elem in documento["anunciosRelacionados"]["anuncioRelacionado"]:
				listarelacionados.append(elem)
	return len(listarelacionados)


#3. Pedir por teclado la denominacion del contrato y mostrar la descripción de los CPV

def descCPV(cad,datos):
	for documento in datos["expediente"]["anuncios"]["anuncio"]:
		lista=[]
		if cad in documento["denominacionContrato"]:
			for elem in documento["clasificacionCPV"]["clasificacionCPVItem"]:
				lista.append(elem["descripcion"])
		for elem in lista:
			return elem
		
#4. Pedir por teclado la fecha de publicación de un anuncio relacionado y te muestra la referencia de publicación del anuncio principal

def referenciarelacionado(cad,datos):
	for documento in datos["expediente"]["anuncios"]["anuncio"]:
		for elem in documento["anunciosRelacionados"]["anuncioRelacionado"]:
			if cad in elem["fechaPublicacion"]:
				return elem["numeroAnuncio"]

#5. Pedir por teclado la fecha de publicación de un anuncio y te muestra el enlace, el tipo y la descripción de los documentos adjuntos

def datosdocumentosadjuntos(cad,datos):
	for documento in datos["expediente"]["anuncios"]["anuncio"]:
		if cad in documento["fechaPublicacion"]:
			for elem in documento["documentosAdjuntos"]["documentoAdjunto"]:
				return elem["descripcion"],elem["tipo"],elem["enlace"]



import json
with open ("anuncios.json") as fichero:
	datos=json.load(fichero)
	while True:
		print('''
			1.-Tipos datos adjuntos
			2.-Contador Anuncios Relacionados
			3.-Descripcion CPVs
			4.-Referencias Anuncios Relacionados
			5.-Datos de los Documentos Adjuntos 
			0.-Salir''')
		opcion=input("Dime la opcion: ")
		if opcion=="1":
			print(Tiposadjuntos(datos))
		elif opcion=="2":
			cad=input("Dime el tipo de contratos(Servicios o Suministros): ")
			while cad not in ("Servicios","Suministros"):
				print("No tengo contratos con ese Tipo")
				cad=input("Dime el tipo de contratos(Servicios o Suministros): ")
			print(contarrelacionados(cad,datos))
		elif opcion=="3":
			cad=input("Dime la denominacion del contrato(ALMACENAMIENTO,Servicio,Suministro): ")
			while cad not in ("ALMACENAMIENTO","Servicio","Suministro"):
				print("No tengo contratos de esa denominacion")
				cad=input("Dime la denominacion del contrato(ALMACENAMIENTO,Servicio,Suministro): ")
			print(descCPV(cad,datos))
		elif opcion=="4":
			cad=input("Dime la fecha de un anuncio relacionado(dia/mes/año): ")
			print(referenciarelacionado(cad,datos))
		elif opcion=="5":
			cad=input("Dime la fecha de publicacion de un anuncio(dia/mes/año): ")
			print(datosdocumentosadjuntos(cad,datos))
		elif opcion=="0":
			print("Adios")
			break
	#cad=input("Dime el tipo de contratos(Servicios o Suministros: ")
	#print(contarrelacionados(cad,datos))
	#cad=input("Dime la denominacion del contrato(ALMACENAMIENTO,Servicio,Suminitro): ")
	#print(descCPV(cad,datos))
	#cad=input("Dime la fecha de un anuncio relacionado: ")
	#print(referenciarelacionado(cad,datos))
	#cad=input("Dime la fecha de publicacion de un anuncio: ")
	#print(datosdocumentosadjuntos(cad,datos))