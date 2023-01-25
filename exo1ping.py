from flask import Flask, request
import sys
import time
import requests

app2 = Flask(__name__)
@app2.route("/pong", methods=["GET"])


def ping():
    reponse2 = requests.get("http://localhost:8080/adresse2")
    r = reponse2.content
    r = str(r)
    print(r)
    print(type(r))
    return "abc"

if __name__ == '__main__':
    app2.run(host='localhost', port=5372)
    


