import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from json import load


with open(os.path.dirname(os.path.abspath(__file__))+"/config/db.json") as dbconfig:
    data = load(dbconfig)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost/pythoncrm'.format(data['username'], data['password'])
db = SQLAlchemy(app)

import API.routes.client
