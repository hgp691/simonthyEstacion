#!/usr/bin/python
import json1
import correo
import log
import objetos


def enviarAlarma(arreglo,setT,setH):
	print "ENVIAR ALARMA"	


def revisarValores():
	log.escribirLog("revisarValores")
	arreglo=[]
	setT=json1.obtenerSetTemp()
	setH=json1.obtenerSetHum()
	#local
	Tlocal=json1.revisarUltimos5Temp("local.csv")
	Hlocal=json1.revisarUltimos5Hum("local.csv")
	if Tlocal > setT or Hlocal > setH :
		a=json1.ultimo("local.csv")
		obj=objetos.sonda(Tlocal,Hlocal,"ESTACION",a.fecha,a.hora)
		arreglo.append(obj)
	else:
		print "Es menor"
	#remotas
	a=json1.obtenerRemotas()
	for remota in a:
		if remota["ACTIVA"] == "YES":
			archivo=str(remota["DIRECCION"])+".csv"
			t=json1.revisarUltimos5Temp(archivo)
			h=json1.revisarUltimos5Hum(archivo)
			if t > setT or h > setH :
				b=json1.ultimo(archivo)
				obj=objetos.sonda(t,h,remota["NOMBRE"],b.fecha,b.hora)
				arreglo.append(obj)
			else:
				print "Remota es menor"
		else:
			print remota["NOMBRE"]+" desactivada"	
	if len(arreglo) > 0:
		enviarAlarma(arreglo,setT,setH)
revisarValores()
