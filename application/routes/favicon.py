# -*- coding: utf-8 -*-

import os
from flask import send_from_directory, current_app

def favicon(filename):
    path = os.path.join(current_app.root_path, 'static', 'img', 'favicon')
    filename = os.path.basename(filename)
    mimetype = 'image/vnd.microsoft.icon' if '.ico' in filename else 'image/png'
    return send_from_directory(path, filename, mimetype=mimetype)
