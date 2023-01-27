from flask import Flask, request
import sys
import time
import requests

adresse1 = "http://localhost:4567"
adresse2 = "http://localhost:5372"

app3 = Flask(__name__)

@app3.route("/adresse1", methods=["GET"])
def serveur1():
    return adresse1

@app3.route("/adresse2", methods=["GET"])
def serveur2():
    return adresse2

if __name__ == '__main__':
    app3.run(host='localhost', port=8080)
    


