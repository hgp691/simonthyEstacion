#!/usr/bin/python

import datetime
import time
import Adafruit_DHT
import enviar
import json

#funcion que obtiene la hora
def obtenerHora():
        hora=time.strftime("%H:%M:%S",time.localtime())
        return hora
#funcion que obtiene la fecha
def obtenerFecha():
        fecha=time.strftime("%Y-%m-%d",time.localtime())
        return fecha

#definicion del sensor
sensor = Adafruit_DHT.DHT11
# conectado a GPIO23
pin = 4
#obtener la lectura
humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
#si la lectura esta bn
if humedad is not None and temperatura is not None:
    #print temperature 
	#print humidity
	with open('datos/GPRMC.json') as data_file:
         	data = json.load(data_file)
                Hora_loc=data["Hora"]
                Fecha_loc=data["Fecha"]
                Lat=data["Latitude "]
               	Lon=data["Longitude"]
                N_S=data["N/S"]
                E/W=data["E/W"]
                cadena=data["cadena"]
                UTC_time=data["UTC time"]
	enviar.enviarDatos("0",obtenerFecha(),obtenerHora(),temperatura,humedad,Hora_loc,Fecha_loc,Lat,Lon,N_S,E_W,cadena,UTC_time)
else:
        print 'Error obteniendo'

