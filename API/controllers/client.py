import os
from flask import request
from json import dumps
from random import randint

from API import app, db
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
                "state": client.state.value,
                "image": app.config['UPLOAD_FOLDER'] + client.image
            }
        }, indent=4)


def getByName(name):
    clients = Client.query.filter_by(name=name).all()
    clientsList = []

    if bool(clients) is False:
        return dumps({
            "success": False,
            "message": "No client found"
        }, indent=4)
    else:
        for client in clients:
                clientsList.append({
                    "id": client.id,
                    "name": client.name,
                    "company": client.company,
                    "state": client.state.value,
                    "image": app.config['UPLOAD_FOLDER'] + client.image
                })

        return dumps({
            "success": True,
            "clients": clientsList
        }, indent=4)


def getByCompany(company):
    clients = Client.query.filter_by(company=company).all()
    clientsList = []

    if bool(clients) is False:
        return dumps({
            "success": False,
            "message": "No client found"
        }, indent=4)
    else:
        for client in clients:
                clientsList.append({
                    "id": client.id,
                    "name": client.name,
                    "company": client.company,
                    "state": client.state.value,
                    "image": app.config['UPLOAD_FOLDER'] + client.image
                })

        return dumps({
            "success": True,
            "clients": clientsList
        }, indent=4)


def getByState(state):
    clients = Client.query.filter_by(state=state).all()
    clientsList = []

    if state not in State.__members__:
        return dumps({
            "succes": False,
            "message": "Wrong state"
        }, indent=4)

    if bool(clients) is False:
        return dumps({
            "success": False,
            "message": "No client found"
        }, indent=4)
    else:
        for client in clients:
                clientsList.append({
                    "id": client.id,
                    "name": client.name,
                    "company": client.company,
                    "state": client.state.value,
                    "image": app.config['UPLOAD_FOLDER'] + client.image
                })

        return dumps({
            "success": True,
            "clients": clientsList
        }, indent=4)


def getAll():
    clients = Client.query.all()
    clientsList = []

    if bool(clients) is False:
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
                    "state": client.state.value,
                    "image": app.config['UPLOAD_FOLDER'] + client.image
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

    if bool(clients) is False:
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
                    "state": client.state.value,
                    "image": app.config['UPLOAD_FOLDER'] + client.image
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
        and 'file' in request.files
        and request.files['file'] != ''
    ):
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = request.form['name'] + str(randint(1, 999999999999)) + '.' + file.filename.rsplit('.', 1)[1]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        client = Client(
            request.form['name'],
            request.form['company'],
            request.form['state'],
            filename
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
        or 'company' in request.form
        or 'state' in request.form
        and client is not None
    ):

        if 'name' in request.form:
            client.name = request.form['name'] or ''

        if 'company' in request.form:
            client.company = request.form['company'] or ''

        if 'state' in request.form:
            if request.form['state'] in State.__members__:
                client.state = State[request.form['state']] or ''
            else:
                return dumps({
                    "success": False,
                    "message": "Wrong state"
                }, indent=4)

        if 'file' in request.files and request.files['file'] != '':
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = client.image.rsplit('.', 1)[0] + '.' + file.filename.rsplit('.', 1)[1]
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

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


# Upload filename check
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
