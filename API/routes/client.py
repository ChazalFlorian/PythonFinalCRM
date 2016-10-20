from API import app
from API.controllers import client


app.add_url_rule('/client/get/<int:id>', 'getClient', client.get, methods=["GET"])

app.add_url_rule('/client/add', 'addClient', client.add, methods=["GET"])

app.add_url_rule('/client/edit/<int:id>', 'editClient', client.edit, methods=["GET"])

app.add_url_rule('/client/delete/<int:id>', 'deleteClient', client.delete, methods=["GET"])
