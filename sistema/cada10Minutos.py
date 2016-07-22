#!/usr/bin/python
import json1
import correo
import log

def revisarComunicacion():
	log.escribirLog("revisarComunicacion")
	cliente=json1.obtenerClienteSMTP()
	if cliente["ENVIAR_COMUNICACION"] == "YES":
		a=json1.obtenerRemotas()
		for sonda in a :
			if sonda["ACTIVA"] == "YES":
				print sonda["NOMBRE"]+" ACTIVA"
				if json1.compararUltimo(sonda["DIRECCION"]):
					print "ENTRADA"
					correo.correoSerial("hgp691@gmail.com",sonda["NOMBRE"])
			else:
				print sonda["NOMBRE"]+" INACTIVA"
		if json1.compararUltimo("local"):
			correo.correoSerial("hgp691@gmail.com","SONDA LOCAL")
revisarComunicacion()	
