import os
from flask import Blueprint, request, abort, session, current_app, send_from_directory
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])

def mkdir_assets(assets_dir):
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

asset_server = Blueprint('asset_server', __name__)

def allowed_filename(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@asset_server.route('image/<path:path>', methods=['GET', 'POST'])
def assets_image(path):
    
    path = secure_filename(path)
        
    if  path == '' or not allowed_filename(path):
        abort(400, "Invalid filename")

    assets_dir = current_app.config['ASSETS_DIR']
    mkdir_assets(assets_dir)
 
    if request.method == 'POST':
        if 'file' not in request.files:
            abort(400, "no file provided")
      
        f = request.files['file']
       
        f.save(os.path.join(assets_dir, path))
        return {'status': 'success'} , 201

    # GET
    return send_from_directory(assets_dir, path)
