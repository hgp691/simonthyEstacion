#!/usr/bin/python

import remota
import obtener
import json1

#obtener.local()

remotas=json1.obtenerRemotas()

for remote in remotas:
	if remote["ACTIVA"]=="YES":
		remota.obtenerRemota(remote)
