#!/usr/bin/python3 
##################################################
## El siguiente script utiliza CPGI , un estándar 
## de programación web que consiste en ejecutar un 
## programa en el servidor y desplegar su resultado 
## hacia el cliente. 
##################################################
## {License_info}
##################################################
## Authors: Jhoan Steven Delgado Villarreal, Andrés Zapata Orozco
## Copyright: Copyright 2019, Proyecto final Sistemas operativos
## Profesor: Juan Felipe Gómez
##################################################
import cgi
import os
import cgitb
cgitb.enable()
# Headers
processRoute="./tmp/process.txt"
os.system('ps -ef > '+processRoute)
fp=open(processRoute,"r")
lines=fp.readlines()
print("Content-Type: text/html")
print()
print("""<html>
<head>
   <title>Processes Monitor</title>
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"/>
</head>
<body>
   <table class="table">
       <thead class="thead-dark">
         <tr>
            <th scope="col">UID</th>
            <th scope="col">PID</th>
            <th scope="col">PPID</th>
            <th scope="col">C</th>
            <th scope="col">STIME</th>
            <th scope="col">TTY</th>
            <th scope="col">TIME</th>
            <th scope="col">CMD</th>
            <th scope="col">TERMINATE?</th>
          </tr>
        </thead>
        <tbody>""")
v=[]
for i in lines:
    v.append(i.split())

print("<form action='' method='get'>")
while True:
  for i in range(1,len(v)):
    print("<tr>")
    for j in range(8):
      print("<td>"+v[i][j]+"</td>")
    print("<td><input type='submit' value='kill' name='"+str(v[i][1])+"'</td>")  
    print("</tr>") 
  break   
print("</form>")
print("""</tbody>
     </table>
     <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
     <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
     <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>""")

form = cgi.FieldStorage()
for i in range(1,len(v)):
  if form.getvalue(str(v[i][1])):
    os.system('kill -9 '+str(v[i][1]))
    print ("<meta http-equiv=\"refresh\" content=\"0; url = http://localhost:8000/cgi-bin/monitor.py\" />")