#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Usage: http://<hostname>[:<prt>]/api/<url>"

@app.route("/example/")
def another_index():
    return "<h1>Hello!!!!</h1>"



app.run(host="0.0.0.0")


