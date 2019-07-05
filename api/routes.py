from flask import Blueprint, jsonify, abort

ambrosia_api = Blueprint('ambrosia_api', __name__)

@ambrosia_api.route('/recipes')
def get_recipes():
    return jsonify({'data': 'abcdefghi'})
