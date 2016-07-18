#!/usr/bin/python
import json
import time

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
#devuelve la fecha y hora actuales sin espacios para nombrar un archivo
def obtenFechaActualArchivo():
	fecha=time.strftime("%Y-%m%d$%H:%M")
	print "nombre del nuevo archivo " +str(fecha)
	return fecha
#devuelve la hora actual del sistema en formato
def obtenFechaActual():
	fecha=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
	print fecha
	return fecha
