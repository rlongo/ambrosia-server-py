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
    data = {'error': str(err)}
    return jsonify(data)


@ambrosia_api.route('/recipes')
def get_recipes():
    tags = request.args.getlist('tag')

    data = api.handlers.get_recipes(storage, tags)
    return jsonify(data)


@ambrosia_api.route('/r/<string:rid>')
def get_recipe(rid=None):
    data = api.handlers.get_recipe(storage, rid)
    return jsonify(data)

@ambrosia_api.route('/r', methods=['POST'])
def add_recipe():
    data = request.get_json()
    rid = api.handlers.add_recipe(storage, data)
    LOGGER.info("Added new recipe rid: %s" % rid)
    return {'rid': rid}, 201

@ambrosia_api.route('/r/<string:rid>/s', methods=['POST'])
def add_stage(rid=None):
    data = request.get_json()
    sid = api.handlers.add_stage(storage, rid, data)
    LOGGER.info("Added new recipe stage sid: %s" % sid)
    return {'sid': sid}, 201
