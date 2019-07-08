from flask import Blueprint, jsonify, abort, request
from api.storage import AmbrosiaStorage
import api.handlers

import logging
from logging import Formatter
LOGGER = logging.getLogger('ambrosia-logger')
handler = logging.StreamHandler()
handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)

ambrosia_api = Blueprint('ambrosia_api', __name__)
storage = AmbrosiaStorage('mongodb://localhost:27017/', 'ambrosia', 'recipes')

@ambrosia_api.errorhandler(Exception)
def handle_unknown_errors(err):
    data = { 'error': str(err) }
    return jsonify(data)

@ambrosia_api.route('/recipes')
def get_recipes():
    headers_only = request.args.get('headers_only', default=True)
    tags = request.args.getlist('tag')

    data = api.handlers.get_recipes(storage, headers_only, tags)
    return jsonify(data)

@ambrosia_api.route('/r', methods=['POST'])
def add_recipe():
    data = request.get_json()
    rid = api.handlers.add_recipe(storage, data)
    LOGGER.info("Added new recipe rid: %s" % rid)
    return { 'rid': rid }, 201


