#!/usr/bin/python
import json
import time
import csv

def obtenerRutaConfiguracion():
	return "/mnt/usb/simonthy/config/"

def obtenerPin():
	ruta = obtenerRutaConfiguracion() + "sensores.json"
	print ruta
	with open(ruta) as data_file:
		data = json.load(data_file)
		return data['PIN_HUMEDAD']
#print obtenerPin()
def obtenerRemotas():
	ruta = obtenerRutaConfiguracion() + "remotas.json"
	with open(ruta) as data_file:
                data=json.load(data_file)
                return data
#print obtenerRemotas()

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
def obtenerSetTemp():
        ruta = obtenerRutaConfiguracion() + "sets.json"
        with open(ruta) as data_file:
                data=json.load(data_file)
                return data["TEMPERATURA"]
def obtenerSetHum():
        ruta = obtenerRutaConfiguracion() + "sets.json"
        with open(ruta) as data_file:
                data=json.load(data_file)
                return data["HUMEDAD"]
def obtenerArreglo(archivo):
        ruta='/mnt/usb/simonthy/datos/'+archivo
        arreglo=[]
        reader=csv.reader(open(ruta,'rb'))
        for index,row in enumerate(reader):
                obj["fecha"]=row[0]
                obj["hora"]=row[1]
                obj["temperatura"]=row[2]
                obj["humedad"]=row[3]
                arreglo.append(obj)
        return arreglo
obtenerArreglo("local.csv")
