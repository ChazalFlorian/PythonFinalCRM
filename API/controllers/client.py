from flask import request
from json import dumps

from API import db
from API.models.client import Client
from API.models.client import State


def get(id):
    client = Client.query.filter_by(id=id).first()

    if client is None:
        return dumps({
            "success": False,
            "message": "Client not found"
        }, indent=4)
    else:
        return dumps({
            "success": True,
            "client": {
                "id": client.id,
                "name": client.name,
                "company": client.company,
                "state": client.state.value
            }
        }, indent=4)


def getAll():
    clients = Client.query.all()
    clientsList = []

    if clients is None:
        return dumps({
            "success": False,
            "message": "Error during clients getting"
        }, indent=4)
    else:
        for client in clients:
                clientsList.append({
                    "id": client.id,
                    "name": client.name,
                    "company": client.company,
                    "state": client.state.value
                })

        return dumps({
            "success": True,
            "clients": clientsList
        }, indent=4)


def getCustom():
    params = {}

    if "name" in request.form:
        params["name"] = request.form['name']

    if "company" in request.form:
        params["company"] = request.form['company']

    if (
        "state" in request.form
        and request.form['state'] in State.__members__
    ):
        params["state"] = request.form['state']
    elif (
        "state" in request.form
        and request.form['state'] not in State.__members__
    ):
        return dumps({
            "success": False,
            "message": "Wrong state"
        }, indent=4)

    if bool(params) is True:
        clients = Client.query.filter_by(**params).all()
    else:
        return dumps({
            "success": False,
            "message": "No parameter given"
        }, indent=4)

    if clients is None:
        return dumps({
            "success": False,
            "message": "Client not found"
        }, indent=4)
    else:
        clientsList = []
        for client in clients:
                clientsList.append({
                    "id": client.id,
                    "name": client.name,
                    "company": client.company,
                    "state": client.state.value
                })

        return dumps({
            "success": True,
            "clients": clientsList
        }, indent=4)


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
        client = Client(
            request.form['name'],
            request.form['company'],
            request.form['state'],
        )

        db.session.add(client)
        db.session.commit()

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
    client = Client.query.filter_by(id=id).first()
    if (
        'name' in request.form
        and 'company' in request.form
        and 'state' in request.form
        and request.form['state'] in State.__members__
        and client is not None
    ):

        client.name = request.form['name']
        client.company = request.form['company']
        client.state = State[request.form['state']]

        db.session.commit()

        return dumps({
            "success": True,
            "client": {
                "id": client.id,
                "name": client.name,
                "company": client.company,
                "state": client.state.value
            }
        }, indent=4)
    elif client is None:
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
    client = Client.query.filter_by(id=id).first()

    if client is None:
        return dumps({
            "success": False,
            "message": "Client not found"
        }, indent=4)
    else:
        db.session.delete(client)
        db.session.commit()
        return dumps({
            "success": True,
        }, indent=4)
