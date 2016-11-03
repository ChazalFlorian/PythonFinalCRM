from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.provider import OAuth2Provider


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://eiron@localhost/pythoncrm'
db = SQLAlchemy(app)

oauth = OAuth2Provider()
oauth.init_app(app)

import API.routes.client
