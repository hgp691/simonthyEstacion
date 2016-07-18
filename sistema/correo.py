#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText 
import datetime
import time

import os
import log
import sys

import json1


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
		mailServer.login(cliente["FROM"],cliente["CLAVE"])
		mailServer.sendmail(cliente["FROM"],to,msj.as_string())
		mailServer.close()
	except:
		res0="Excepcion 0 correo.correo ->",sys.exc_info()[0]
		print res0
		res="Excepcion 1 correo.correo -> ",sys.exc_info()[1]
		print res

correo("Hola mundo","Este es el texto","hgp691@gmail.com")
