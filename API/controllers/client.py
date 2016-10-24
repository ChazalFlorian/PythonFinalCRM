from flask import request
from json import dumps

from API.models.clients import Clients
from API.models.client import State


def get(id):
    clients = Clients()

    for client in clients.container:
        if client.id == id:
            return dumps({
                "success": True,
                "client": {
                    "id": client.id,
                    "name": client.name,
                    "company": client.company,
                    "state": client.state.value
                }
            }, indent=4)

    return dumps({
        "success": False,
        "message": "Client not found"
    }, indent=4)


def getAll():
    clients = Clients()
    clientsList = []

    for client in clients.container:
            clientsList.append({
                "id": client.id,
                "name": client.name,
                "company": client.company,
                "state": client.state.value
            })

    return dumps(clientsList, indent=4)


# Post parameters :
#    name (string)
#    company (string)
#    state ('prospect' | 'inProgress' | 'finished' | 'partner')
#
def add():
    if (
        'name' in request.form
        and 'company' in request.form
        and 'state' in request.form
        and request.form['state'] in State.__members__
    ):
        clients = Clients()
        client = clients.addClient(
            request.form['name'],
            request.form['company'],
            request.form['state']
        )

        return dumps({
            "success": True,
            "client": {
                "id": client.id,
                "name": client.name,
                "company": client.company,
                "state": client.state.value
            }
        }, indent=4)
    else:
        return dumps({
            "success": False,
            "message": "Missing parameters or wrong state"
        }, indent=4)


# Post parameters :
#    name (string)
#    company (string)
#    state ('prospect' | 'inProgress' | 'finished' | 'partner')
#
def edit(id):
    if (
        'name' in request.form
        and 'company' in request.form
        and 'state' in request.form
        and request.form['state'] in State.__members__
    ):
        clients = Clients()

        for client in clients.container:
            if client.id == id:
                client.name = request.form['name']
                client.company = request.form['company']
                client.state = State[request.form['state']]

                return dumps({
                    "success": True,
                    "client": {
                        "id": client.id,
                        "name": client.name,
                        "company": client.company,
                        "state": client.state.value
                    }
                }, indent=4)

        return dumps({
            "success": False,
            "message": "Client not found"
        }, indent=4)
    else:
        return dumps({
            "success": False,
            "message": "Missing parameters or wrong state"
        }, indent=4)


def delete(id):
    clients = Clients()

    for client in clients.container:
        if client.id == id:
            clients.container.remove(client)

            return dumps({
                "success": True
            }, indent=4)

    return dumps({
        "success": False,
        "message": "Client not found"
    }, indent=4)
