from flask import Flask, request
import sys
import time
import requests

app1 = Flask(__name__)

@app1.route("/ping", methods=["GET"])
def pong():
    requests.get("http://localhost:4567/ping")
    return "pong sent"

def getadresse():
    r = requests.get("http://localhost:8080/adresse")
    return r

if __name__ == '__main__':
    print("app1")
    app1.run(host='localhost', port=4567)
