import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from json import load

with open(os.path.dirname(os.path.abspath(__file__))+"/config/db.json") as dbconfig:
    data = load(dbconfig)

# Directories setting
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
CDN_PATH = PARENT_DIR + '/CDN/images/'
TEMPLATE_PATH = PARENT_DIR + "/GUI/"

app = Flask(__name__, template_folder=TEMPLATE_PATH)

# File Upload
app.config['UPLOAD_FOLDER'] = CDN_PATH

# MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost/pythoncrm'.format(data['username'], data['password'])
db = SQLAlchemy(app)

# import routes
import API.routes.client
import API.routes.SpreadSheet.spreadsheet
