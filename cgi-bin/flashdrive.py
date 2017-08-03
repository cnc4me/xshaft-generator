#!C:\Python27\python.exe

from os.path import exists
from json import dumps


print "Content-type: application/json"
print
print dumps({"found": exists("E:\\")})
