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

#4. Pedir por teclado la fecha de publicación de un anuncio relacionado y te muestra la referencia de publicación del anuncio principal

#5. Pedir por teclado la fecha de publicación de un anuncio y te muestra el enlace, el tipo y la descripción de los documentos adjuntos
import json
with open ("anuncios.json") as fichero:
	datos=json.load(fichero)
	cad=input("Dime el tipo de contratos(Servicios o Suministros: ")
	print(contarrelacionados(cad,datos))

	