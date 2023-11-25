import requests
import json
import socket

while True:
    domain=input("Inserisci il dominio: ")
    url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains?children_only=false&include_inactive=false"
    headers = {
    "accept": "application/json",
    "APIKEY": "SECURITY_TRAILS_API_KEY"
    }
    response = requests.get(url, headers=headers)
    jsondata = json.loads(response.text)
    doms = list(dict.fromkeys(jsondata["subdomains"]))
    print("In tutto conto "+str(len(doms))+" sottodomini\n\n\n")
    for sub in doms:
        hostname = sub+"."+domain
        ip = "N/A"
        try:
            ip = socket.gethostbyname(hostname)
        except Exception:
            print(hostname+"\tN/A")
        print(hostname+"\t"+str(ip))

