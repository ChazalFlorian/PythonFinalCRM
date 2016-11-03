import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from json import load
from flask_oauthlib.provider import OAuth2Provider


with open(os.path.dirname(os.path.abspath(__file__))+"/config/db.json") as dbconfig:
    data = load(dbconfig)

app = Flask(__name__)

# MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost/pythoncrm'.format(data['username'], data['password'])
db = SQLAlchemy(app)

# File upload
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
CDN_PATH = PARENT_DIR + '/CDN/images/'
app.config['UPLOAD_FOLDER'] = CDN_PATH


import API.routes.client
import API.routes.SpreadSheet.spreadsheet
