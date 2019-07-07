#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_cors import CORS

from api import ambrosia_api

app = Flask(__name__)
app.register_blueprint(ambrosia_api, url_prefix='/api/v1')
CORS(app)

@app.route('/')
def route_home():
    return "Hello World"

@app.route('/echo/<word>')
def route_echo(word):
    data = "Hello %s" % word
    return jsonify({'msg': data})

@app.route('/data', methods=['POST'])
def route_data():
    print(request.form)
    content = {}
    return content, 201

