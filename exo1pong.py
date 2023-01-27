from flask import Flask, request
import sys
import time
import requests

app1 = Flask(__name__)

@app1.route("/ping", methods=["GET"])
def pong():
    reponse1=requests.get("http://localhost:8080/adresse1")
    r1=reponse1.text
    requests.get(r1+"/ping")
    return "pong sent"

if __name__ == '__main__':
    app1.run(host='localhost', port=4567)
