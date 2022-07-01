

import collections
from collections import namedtuple

planet=namedtuple("planet",["name",
"alternatenames",
"aphelion",
"perihelion",
"semimajoraxis",
"eccentricity",
"orbitalperiod",
"averageorbitalspeed",
"meananomaly",
"inclination",
"satellites"])

earth=planet("EARTH",
"Terra Tellus Gaia",
"152100000km",
"14709500km",
"149598023km",
"0.0167086",
"365.256.363004d",
"29.78kmp/s",
"358.617",
"7.155",
"moon")

print(earth,"\n")
#print("PLANET NAME:",earth.name,"\nALTERNATIVE NAMES:",earth.alternatenames,"\nAPHELION:",earth.aphelion,"\nPERHELION",earth.perihelion,"\nSEMI-MAJOR-AXIS:",earth.semimajoraxis,"\nECCENTRICITY:",earth.eccentricity,"\nORBITAL PERIOD:",earth.orbitalperiod,"\nMEAN ANOMALY",earth.meananomaly,"\nINCLINATION:",earth.inclination,"\nSATELLITES:",earth.satellites)
#first way to access to namedtuple elements
print("PLANET NAME:",earth[0])
#second way to access to namedtuple elements
print("PLANET NAME:",earth.name)
#thrid way to access elements
print("PLANET NAME:",getattr(earth,"name"))
#first way to access to namedtuple elements
print("ALTERNATIVE NAMES:",earth[1])
#second way to access to namedtuple elements
print("ALTERNATIVE NAMES:",earth.alternatenames)
#thrid way to access elements
print("ALTERNATIVE NAMES:",getattr(earth,"alternatenames"))
#first way to access to namedtuple elements
print("APHELION:",earth.aphelion)
#second way to access to namedtuple elements
print("APHELION:",earth[2])
#thrid way to access elements
print("APHELION:",getattr(earth,"aphelion"))
#first way to access to namedtuple elements
print("PERIHELION:",earth.perihelion)
#second way to access to namedtuple elements
print("PERIHELION:",earth[3])
#thrid way to access elements
print("PERIHELION:",getattr(earth,"perihelion"))
#****************
#||| _make() ||||
#----------------
#make method is used to make a namedtuple from a list
mars=["MARS","REDPLANET","249261000KM","206650000","227939366km","0.0934","686.980d","779.94D","19.412","1.850","PHOBOS DEIMOS"]
print(planet._make(mars))
#print("PLANET NAME:",mars.name)
#print("SATELLITES:",mars.satellites)
#print("ALTERNATIVE NAMES:",mars.alternatenames)
#****************
#|| _asdict() ||
#----------------
mydict={}
mydict=earth._asdict().copy()
print(mydict.keys())
print(mydict.values())

#*************
#|| **||
#--------------
jupiter={"name":"JUPITER","alternatenames":"GURU SPACEFILTER","aphelion":"816.363gm","perihelion":"740.595gm","semimajoraxis":"778.479gm","eccentricity":"0.0489","orbitalperiod":"11.862","averageorbitalspeed":"398.88d","meananomaly":"20.020","inclination":"1.303","satellites":"Ganymede IO Callisto Carme EUROPA"}
#jupiterdict={}
#jupiterdict=planet(**jupiter).copy()
print(planet(**jupiter))
#print(jupiterdict.values())
#print(jupiter.name)

#*************8
#|| _fields ||
#-------------
#returns the fields in the namedtuple strucutre 
print(earth._fields)

#******************
#|| _replace()   ||
#------------------
earth._replace(satellites="MOON MANMADE CARTOSAT OCEANSAT")
print(earth.satellites)
print(earth[10])
print(getattr(earth,"satellites"))


