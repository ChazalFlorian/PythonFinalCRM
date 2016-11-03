import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.provider import OAuth2Provider


app = Flask(__name__)

# MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://eiron@localhost/pythoncrm'
db = SQLAlchemy(app)

# OAuth
oauth = OAuth2Provider()
oauth.init_app(app)

# File upload
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
CDN_PATH = PARENT_DIR + '/CDN/images/'
app.config['UPLOAD_FOLDER'] = CDN_PATH

import API.routes.client
