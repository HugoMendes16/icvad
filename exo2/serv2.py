from flask import Flask, request, jsonify
import requests

app2 = Flask(__name__)

cpt1 = 0
cpt2 = 0

#Envoie de mon adresse au serveur 3 
my_adress = "http://localhost:5372"
server3_adress = "http://localhost:8080/adresse2"
data3 = {"adress2" : my_adress}
r2 = requests.post(server3_adress, json=data3)

@app2.route("/", methods=["GET"])
def start():
    return "Acceuil Serveur 2"

#Fonction qui récupere l'adresse du serveur 1 depuis le serveur 3 et
@app2.route("/pong", methods=["GET"])
def ping():
    server1 = requests.get("http://localhost:8080/send_adresse1")
    requests.get(server1.text+"/pong")
    return "ping sent" 

"""
@app2.route("/test", methods=["GET"])
def voircpt():
    tmp = requests.get("http://localhost:4567/cpt1")
    print("tmp = ", tmp.text)
    print("type tmp = " , type(tmp.text))
    print("type tmp int = " , type(int(tmp.text)))
    print("tmp en int = " , int(tmp.text))
    return "voircpt"
"""

if __name__ == '__main__':
    app2.run(host='serveur2', port=5372)
    


