from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:razor1911@localhost/pythoncrm'
db = SQLAlchemy(app)

import API.routes.client
import API.routes.SpreadSheet.spreadsheet
