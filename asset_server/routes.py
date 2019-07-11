import os
from flask import Blueprint, request, abort, session, send_from_directory

UPLOAD_DIR='/tmp/ambrosia'

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

asset_server = Blueprint('asset_server', __name__)

@asset_server.route('image/<path:path>', methods=['GET', 'POST'])
def assets_image(path):

    if request.method == 'POST':
        if 'file' not in request.files:
            abort(400, "no file provided")
        f = request.files['file']
        f.save(os.path.join(UPLOAD_DIR, path))
        return {'status': 'success'} , 201

    # GET
    return send_from_directory(UPLOAD_DIR, path)
