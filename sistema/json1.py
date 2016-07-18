#!/usr/bin/python
import json

def obtenerRutaConfiguracion():
	return "../config/"

def obtenerPin():
	ruta = obtenerRutaConfiguracion() + "sensores.json"
	print ruta
	with open(ruta) as data_file:
		data = json.load(data_file)
		return data['PIN_HUMEDAD']
def obtenerClienteSMTP():
	ruta = obtenerRutaConfiguracion() + "clienteSMTP.json"
	with open(ruta) as data_file:
		data=json.load(data_file)
		return data
def obtenerCientesCorreo():
	ruta = obtenerRutaConfiguracion() + "enviarA.json"
	with open(ruta) as data_file:
		data=json.load(data_file)
		return data

print obtenerCientesCorreo()[0]["EMAIL"]
