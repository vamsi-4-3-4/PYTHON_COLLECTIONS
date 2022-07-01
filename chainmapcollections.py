import collections
from collections import ChainMap
mydicta={"apple":"ios","vivo":"funtouch"}
mydictb={"go":"beego"}
mydictc=ChainMap(mydicta,mydictb)
mychild={"server":"tomcat"}
mydicte=mydictc.new_child(mychild)
print("NEW CHILD\n",mydicte)
print("CHAIN MAP\n",mydictc)
print("\nPARENTS:",list(mydictc.parents))
print("\nMAPS:",list(mydictc.maps))
print("\nKEYS:",list(mydictc.keys()))
print("\nVALUES:",list(mydictc.values()))
print("\nTYPE OF THE MYDICTC")
print(type(mydictc))
print("\nACCESSING ELEMENT")
print("VALUE IN APPLE KEY:",mydictc["apple"])
print("\nREVERSING THE CHAINMAP")
mydictd=list(reversed(mydictc.maps))
print(mydictd)




