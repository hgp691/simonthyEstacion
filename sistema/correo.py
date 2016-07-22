#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText 
import datetime
import time

import os
import log
import sys

import json1
import socket


def correo(subject,text,to):
	try:
		cliente=json1.obtenerClienteSMTP()
		print cliente["DIRECCION"]
		msj=MIMEText(text,'html')
		msj['Subject']=subject
		msj['From']="simonthy_toberin@colvista.com"
		msj['To']=to
		#mailServer=smtplib.SMTP('192.168.1.15',25)
		mailServer=smtplib.SMTP(cliente["DIRECCION"],cliente["PUERTO"])
		mailServer.ehlo()
		mailServer.starttls()
		mailServer.ehlo()
		print cliente["FROM"]+" "+cliente["CLAVE"]
		mailServer.login(cliente["FROM"],cliente["CLAVE"])
		mailServer.sendmail(cliente["FROM"],to,msj.as_string())
		mailServer.close()
	except:
		res0="Excepcion 0 correo.correo ->",sys.exc_info()[0]
		print res0
		res="Excepcion 1 correo.correo -> ",sys.exc_info()[1]
		print res
		log.escribirLog(res0)
		log.escribirLog(res)

#correo("Hola mundo","Este es el texto","hgp691@gmail.com")
#envia el correo de inicio apenas se ejecuta el sistema
def inicio(to):
    	asunto="Se ha reiniciado el sistema"
    	#a=netifaces.ifaddresses('eth0')
	a=([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
    	#a="prueba"
	fecha=json1.obtenFechaActual()
	texto="<html><h1>REINICIO DEL SISTEMA<h1><br>"
    	texto="Se ha reiniciado el sistema a las " + str(fecha) +".<br>La direccion del sistema es: <br><i>" + str(a)+"</i><br><br>"
	#a=os.path.getsize("/mnt/usb/dataCenter/data/datos/datos.csv")
	#texto=texto+"El tamano del archivo es: \n"+str(a)+" bytes.<br><br>"
	texto=texto+"</html>"
    	if correo(asunto,texto,to):
		print "envio de correo de inicio realizado con exito"
                return True
    	else:
		print "no se pudo enviar correo de inicio"
        	return False

def correoSerial(to,sonda):
	fecha=json1.obtenFechaActual()
	asunto="ALARMA comunicacion serial !!!"
	texto="<html><h1>ALARMA SERIAL</h1>\n<br>\n<br>"
	texto=texto+"Fecha de alarma:  "+str(fecha)+"\n<br>\n<br>"
	texto=texto+"<br>Hay un problema grave con la comunicacion,intente reiniciar el sistema."
	texto=texto+'De no solucionarse por favor reporte la falla de la sonda <i>'+sonda+'</i> al CES.<br><br>SIMONTHy continuara registrando el monitoreo con los sensores ubicados en el RACK.<br><br>'
	texto=texto+"</html>"
	correo(asunto,texto,to)
		
