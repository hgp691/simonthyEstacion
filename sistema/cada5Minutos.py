#!/usr/bin/python
import json1
import correo
import log
import objetos

def revisarValores():
	setT=json1.obtenerSetTemp()
	setH=json1.obtenerSetHum()
	#local
	Tlocal=json1.revisarUltimos5Temp("local.csv")
	Hlocal=json1.revisarUltimos5Hum("local.csv")
	print str(Tlocal)+"  "+str(Hlocal)
revisarValores()
