from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://eiron@localhost/pythoncrm'
db = SQLAlchemy(app)

import API.routes.client
