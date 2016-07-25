#!/usr/bin/python
import json1
import correo
import log
import objetos


def textoSonda(sonda,setT,setH):
	texto="<tr>"
	texto+="<td>"+sonda.nombre+"</td>"
	if sonda.temperatura != "DESACTIVADA":
		if sonda.temperatura > setT :
			texto+="<td><strong style='color:red'>"+str(sonda.temperatura)+" C</strong></td>"
		else:
			texto+="<td><strong style='color:green'>"+str(sonda.temperatura)+" C</strong></td>"
		if sonda.humedad > setH:
			texto+="<td><strong style='color:red'>"+str(sonda.humedad)+" RH</strong></td>"
		else:
			texto+="<td><strong style='color:green'>"+str(sonda.humedad)+" RH</strong></td>"
		texto+="<td>"+sonda.FechaUltimoDato+" "+sonda.HoraUltimoDato+"</td>"
	else:
		texto+="<td><strong style='color:yellow'>"+str(sonda.temperatura)+"</strong></td>"
		texto+="<td><strong style='color:yellow'>"+str(sonda.humedad)+"</strong></td>"
	texto+="</tr>"
	return texto

def enviarCorreoReporte(arreglo,setT,setH):
	print len(arreglo)
	asunto="REPORTE DE ESTADO"
	texto='<html><h1>REPORTE DE ESTADO</h1>'
	texto+="<table>"
	texto+="<tr>"
	texto+="<th>NOMBRE SONDA:</th>"
	texto+="<th>TEMPERATURA (SET:"+str(setT)+" C)</th>"
	texto+="<th>HUMEDAD (SET:"+str(setH)+" RH)</th>"
	texto+="<th>FECHA ULTIMO DATO:</th>"
	texto+="</tr>"
	for sonda in arreglo:
		texto+=textoSonda(sonda,setT,setH)
	texto+="</table>"
	texto+="</html>"
#	print texto
	clientes=json1.obtenerCientesCorreo()
	for cliente in clientes:
		correo.correo(asunto,texto,cliente["EMAIL"])

def enviarReporte():
	log.escribirLog("enviarReporte")
	arreglo=[]
	setT=json1.obtenerSetTemp()
	setH=json1.obtenerSetHum()
	#local
	Tlocal=json1.revisarUltimos5Temp("local.csv")
	Hlocal=json1.revisarUltimos5Hum("local.csv")
	a=json1.ultimo("local.csv")
	obj=objetos.sonda(Tlocal,Hlocal,"ESTACION",a.fecha,a.hora)
	arreglo.append(obj)
	#remotas
	a=json1.obtenerRemotas()
	for remota in a:
		if remota["ACTIVA"] == "YES":
			archivo=str(remota["DIRECCION"])+".csv"
			t=json1.revisarUltimos5Temp(archivo)
			h=json1.revisarUltimos5Hum(archivo)
			b=json1.ultimo(archivo)
			obj=objetos.sonda(t,h,remota["NOMBRE"],b.fecha,b.hora)
			arreglo.append(obj)
		else:
			obj=obj=objetos.sonda("DESACTIVADA","DESACTIVADA",remota["NOMBRE"],"DESACTIVADA","DESACTIVADA")
			arreglo.append(obj)
	if len(arreglo) > 0:
		enviarCorreoReporte(arreglo,setT,setH)

enviarReporte()
