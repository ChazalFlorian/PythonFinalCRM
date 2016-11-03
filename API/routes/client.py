from API import app
from API.controllers import client


app.add_url_rule(
    '/client/get/<int:id>',
    'getClient',
    client.get,
    methods=["GET"]
)

app.add_url_rule(
    '/client/get/name/<string:name>',
    'getClientsByName',
    client.getByName,
    methods=["GET"]
)

app.add_url_rule(
    '/client/get/company/<string:company>',
    'getClientsByCompany',
    client.getByCompany,
    methods=["GET"]
)

app.add_url_rule(
    '/client/get/state/<string:state>',
    'getClientsByState',
    client.getByState,
    methods=["GET"]
)

app.add_url_rule(
    '/client/get',
    'getClients',
    client.getAll,
    methods=["GET"]
)

app.add_url_rule(
    '/client/get',
    'getCustomClients',
    client.getCustom,
    methods=["POST"]
)

app.add_url_rule(
    '/client/add',
    'addClient',
    client.add,
    methods=["PUT"]
)

app.add_url_rule(
    '/client/edit/<int:id>',
    'editClient',
    client.edit,
    methods=["POST"]
)

app.add_url_rule(
    '/client/delete/<int:id>',
    'deleteClient',
    client.delete,
    methods=["DELETE"]
)
