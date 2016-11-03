from API import app
from API.controllers.SpreadSheet import spreadsheet

app.add_url_rule(
    '/spreadsheet/export/',
    'exportSpreadSheet',
    spreadsheet.exportDB(),
    methods=["GET"]
)

app.add_url_rule(
    '/spreadsheet/import/',
    'importSpreadSheet',
    spreadsheet.importDB(),
    methods=["GET"]
)
