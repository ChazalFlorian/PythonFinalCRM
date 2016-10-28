from flask import Flask
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
oauth = OAuth2Provider()
oauth.init_app(app)

import API.routes.client
