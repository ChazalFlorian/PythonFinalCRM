import json


class Client:

    user = ""

    client_id = ""
    client_secret = ""

    def __init__(self):
        with open(PARENT_DIR+"/config/config.json") as data_file:
            data = json.load(data_file)
            client_id = data["client_id"]
            client_secret = data["client_secret"]

    is_confidential = true

    _redirect_uris = ""
    _default_scopes = ""

    @property
    def client_type(self):
        if self.is_confidential:
            return 'confidential'
        return 'public'

    @property
    def redirect_uris(self):
        if self._redirect_uris:
            return self._redirect_uris.split()
        return []

    @property
    def default_redirect_uri(self):
        return self.redirect_uris[0]

    @property
    def default_scopes(self):
        if self._default_scopes:
            return self._default_scopes.split()
        return []
