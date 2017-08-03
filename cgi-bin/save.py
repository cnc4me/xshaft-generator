#!C:\Python27\python.exe

import os, subprocess, cgitb, cgi, shutil, json
cgitb.enable()

storage    = "C:\Mcam9\Mill\NC\XSHAFTS\\"
flashdrive = "E:\\"

form     = cgi.FieldStorage()
program  = form.getvalue('program')
filename = form.getvalue('filename')
filepath = storage + filename + ".NC"

programFile = file(filepath, "w+")
programFile.write(program)
programFile.close()

if os.path.exists(flashdrive):
    shutil.copy(filepath, flashdrive)
    copied = 1
else:
    copied = 0

#os.startfile(filepath)
#subprocess.Popen("open.bat " + filepath)
#C:\Mcam9\Common\Editors\Cedit\CIMCOEdit.exe

print "Content-type: application/json"
print
print json.dumps({ "copied" : copied, "location" : filepath })
