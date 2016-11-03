from API import db
from datetime import datetime
from API.models.client import Client
from API.models.SpreadSheet.wizard import spreadWizard

client_columns = Client.__table__.columns.keys()
wizard = spreadWizard()


def exportDB(spreadURL=""):
    print('test')

    clients = Client.query.all()

    if(spreadURL != ""):
        spread = wizard.gc.open_by_url(spreadURL)
    else:
        spread = wizard.gc.open_by_key(wizard.defaultWKS)

    worksheet = spread.add_worksheet(title="PythonCRM | "
                                     + str(datetime.now()),
                                     rows=(len(clients)+1),
                                     cols=len(client_columns))

    for i, client in enumerate(clients):
        if (i == 0):
            for j, columnName in enumerate(client_columns):
                worksheet.update_cell(i+1, j+1, columnName)

        for k, colValue in enumerate(client_columns):
                worksheet.update_cell((i+2),
                                      (k+1),
                                      client.__dict__[str(colValue)])


def importDB(spread="", worksheet=1, header=True):

    if(spread != ""):
        spread = wizard.gc.open_by_url(spread)
    else:
        spread = wizard.gc.open_by_key(wizard.defaultWKS)

    worksheet = spread.get_worksheet(worksheet)
    values = worksheet.get_all_values()

    if(header):
        del values[0]

    print(values)

    for index, value in enumerate(values):
        if(Client.query.filter_by(id=value[0]).first()):
            client = Client(
                            value[1],
                            value[2],
                            value[3][6:]
                            )

            db.session.add(client)
            db.session.commit()
