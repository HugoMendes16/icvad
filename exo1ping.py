from flask import Flask, request
import sys
import time
import requests

app2 = Flask(__name__)
@app2.route("/pong", methods=["GET"])

def ping():
    requests.get("http://localhost:5372/pong")
    return "ping sent"

if __name__ == '__main__':
    app2.run(host='localhost', port=5372)
    


