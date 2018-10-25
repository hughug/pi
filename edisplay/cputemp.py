#!/usr/bin/python
# -*- coding: utf-8 -*-
# this program reads the cpu temperature

import io 

def gettemp():
   f = open("/sys/class/thermal/thermal_zone0/temp", "r") 
   t = f.readline ()
   CelsiusTemp = float(t)/1000
   return CelsiusTemp

#cputemp = "CPU: "+'%.1f'%gettemp()+'°C'
#print(cputemp)
