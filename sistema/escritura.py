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

def subir(temperatura,humedad,archivo):
    	try:
        	fecha=time.strftime("%Y-%m-%d",time.localtime())
    		hora=time.strftime("%H:%M:%S",time.localtime())
    		fila=[fecha,hora,temperatura,humedad]
		ruta='/mnt/usb/simonthy/datos/'+archivo+'.csv'
        	#archivo=open(r'/mnt/usb/simonthy/datos/local.csv','ab')
 	    	archivo=open(ruta,'ab')
		print "Se abrio el archivo"
	    	escribir=csv.writer(archivo)
        	escribir.writerow(fila)
        	archivo.close()
        	print "Dato escrito"
	except:
        	resp="Excepcion subirLocal -> ",sys.exc_info()[1]
        	print resp
        	log.escribirLog(resp)
        
    
#subir(2.5,12.6,"local")
