#!/usr/bin/python
import csv
import os
import time
import log

def comprobarExistencia():
	try:
        archivo=open('/mnt/usb/simonthy/datos/local.csv','r')
    	print "El archivo existe"
    	archivo.close()
    except:
        print "El archivo no existe, Se creara"
    	archivo=open('/mnt/usb/simonthy/datos/local.csv','wb')
   	 	archivo.close()
    	print os.system("df -h")
#comprobarExistencia()

def subirLocal(temperatura,humedad):
	print "Recibio "+a+"--"+b+"--"+c+"--"+d;
    try:
        fecha=time.strftime("%Y-%m-%d",time.localtime())
    	hora=time.strftime("%H:%M:%S",time.localtime())
    	fila=[fecha,hora,temperatura,humedad]
        archivo=open(r'/mnt/usb/simonthy/datos/local.csv','ab')
 	    print "Se abrio el archivo"
	    escribir=csv.writer(archivo)
        escribir.writerow(fila)
        archivo.close()
        print "Dato escrito"
        return True
    except:
        resp="Excepcion subirLocal -> ",sys.exc_info()[1]
        print resp
        log.escribirLog(resp)
     	return False
        
    
#subir(2.5,34.5,34.7,12.6)
