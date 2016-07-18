#!/usr/bin/python

import datetime
import time
import Adafruit_DHT
import escritura
import json1

#funcion que obtiene la hora
def obtenerHora():
        hora=time.strftime("%H:%M:%S",time.localtime())
        return hora
#funcion que obtiene la fecha
def obtenerFecha():
        fecha=time.strftime("%Y-%m-%d",time.localtime())
        return fecha

def local():
	#definicion del sensor
	sensor = Adafruit_DHT.DHT11
	# conectado a GPIO23
	pin = json1.obtenerPin()
	print pin
	#obtener la lectura
	humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
	#si la lectura esta bn
	if humedad is not None and temperatura is not None:
		print temperature 
		print humidity
	else:
        	print 'Error obteniendo'

