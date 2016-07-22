#!/usr/bin/python
import json
import time
import csv
import objetos
from datetime import datetime
from datetime import timedelta


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
                obj = objetos.TyH(row[0],row[1],row[2],row[3])
                arreglo.append(obj)
        return arreglo
def cantidadFilasArchivo(ruta):
        try:
                rut="/mnt/usb/simonthy/datos/"+ruta
                i=0
                reader=csv.reader(open(rut,'rb'))
                for index,row in enumerate(reader):
                        i+=1
                return i
        except:
                resp="Excepcion json1.cantidadFilasArchivo -> ",sys.exc_info()[1]
                return "Nope"
                print resp
def revisarUltimos5Temp(ruta):
        if cantidadFilasArchivo(ruta) > 5:
                a=obtenerArreglo("local.csv")
                b=a[len(a)-1]
                c=a[len(a)-2]
                d=a[len(a)-3]
                e=a[len(a)-4]
                f=a[len(a)-5]
                g = (float(b.temperatura)+float(c.temperatura)+float(d.temperatura)+float(e.temperatura)+float(f.temperatura))/5
                return g
        else:
                return 0
def revisarUltimos5Hum(ruta):
        if cantidadFilasArchivo(ruta) > 5:
                a=obtenerArreglo("local.csv")
                b=a[len(a)-1]
                c=a[len(a)-2]
                d=a[len(a)-3]
                e=a[len(a)-4]
                f=a[len(a)-5]
                g = (float(b.humedad)+float(c.humedad)+float(d.humedad)+float(e.humedad)+float(f.humedad))/5
                return g
        else:
                return 0
def ultimo(archivo):
	a=obtenerArreglo(archivo)
	return a[len(a)-1]
def compararUltimo(remota):
	a=ultimo(str(remota)+".csv")
	fecha = a.fecha+" "+a.hora
	fecha1=datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
	print "Ultimo dato: "
	print fecha1
	fechaActual=datetime.now()
	print "Fecha actual:"
	print fechaActual
	esperada = fechaActual-timedelta(minutes=5)
	return fecha1 < esperada
#print compararUltimo("local")
