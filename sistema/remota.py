#!/usr/bin/python

import serial
import time
import sys
import log


def obtenerRemota(obj):
	puerto=obj["PUERTO"]
	velocidad=obj["VELOCIDAD"]
	try:
		ser = serial.Serial(puerto, velocidad, timeout=2)
		ser.close()
		ser.open()
		ser.write("@001")
		time.sleep(3)
		ser.flush()
		print "Imprimiendo dato"
		read_val=ser.read(size=64)
		print read_val
		ser.flush()
		print "* "+str(len(read_val))
		ser.close()
	except serial.SerialException:
		print "Exeption"	
		res0="Excepcion 0 correo.correo ->",sys.exc_info()[0]
      		print res0
        	res="Excepcion 1 correo.correo -> ",sys.exc_info()[1]
        	print res
        	log.escribirLog(res0)
        	log.escribirLog(res)

