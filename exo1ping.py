from flask import Flask, request
import sys
import time
import requests

app2 = Flask(__name__)

@app2.route("/pong", methods=["GET"])
def ping():
    reponse2 = requests.get("http://localhost:8080/adresse2")
    r2 = reponse2.text
    requests.get(r2+"/pong")
    return "ping sent"

if __name__ == '__main__':
    app2.run(host='localhost', port=5372)
    


