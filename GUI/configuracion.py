#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

dirConfig=""

def configurarSMTP():
	with open(dirConfig+'clienteSMTP.json') as data_file:	
		data = json.load(data_file)
		comando="sudo bash configurarSMTP.sh "+data['FROM']+" "+data['CLAVE']+" "+data['DIRECCION']+" "+str(data['PUERTO'])+" "+data['START_TLS']+" "+data['ENVIAR']
		print comando
configurarSMTP()
