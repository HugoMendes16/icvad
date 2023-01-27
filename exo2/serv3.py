from flask import Flask, request, jsonify
import requests


app3 = Flask(__name__)
server1=""
server2=""

@app3.route("/", methods=["GET"])
def start():
    return "Acceuil Serveur 3"

@app3.route("/adresse1", methods=["POST"])
def register_serveur1():
    global server1
    data = request.get_json()
    server1 = data.get("adress1")
    return jsonify({"status": "success"})

@app3.route("/adresse2", methods=["POST"])
def register_serveur2():
    global server2
    data = request.get_json()
    server2 = data.get("adress2")
    return jsonify({"status": "success"})



@app3.route("/send_adresse2", methods=["GET"])
def get_serveur2():
    global server2
    print("serveur 2 = " , server2)
    return server2


@app3.route("/send_adresse1", methods=["GET"])
def get_serveur1():
    global server1
    print("serveur 1 = " , server1)
    return server1
    


if __name__ == '__main__':
    app3.run(host='serveur3', port=8080)
    


