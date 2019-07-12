#!/usr/bin/env python3
from flask import Flask, request, jsonify, config
from flask_cors import CORS

from api import ambrosia_api
from asset_server import asset_server

app = Flask(__name__)
app.config['ASSETS_DIR'] = '/tmp/ambrosia'

app.register_blueprint(ambrosia_api, url_prefix='/api/v1')
app.register_blueprint(asset_server, url_prefix='/assets')
CORS(app)

