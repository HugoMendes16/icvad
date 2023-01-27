from flask import Flask, request
import requests

app1 = Flask(__name__)

cpt1 = 0

#Envoie de mon adresse au serveur 3
my_adress = "http://localhost:4567"
server3_adress = "http://serveur3/adresse1"
data1 = {"adress1" : my_adress}
r1 = requests.post(server3_adress, json=data1)

@app1.route("/", methods=["GET"])
def start():
    return "Acceuil Serveur 1"

@app1.route("/ping", methods=["GET"])
def pong():
    server2 = requests.get("http://localhost:8080/send_adresse2")
    requests.get(server2.text+"/ping")
    return "pong sent"

if __name__ == '__main__':
    app1.run(host='serveur1', port=4567)
