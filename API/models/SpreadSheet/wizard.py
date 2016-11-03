import sys
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class spreadWizard():

    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        sys.path[0] + "/config/config.json",
        scope
    )

    gc = gspread.authorize(credentials)

    with open(sys.path[0] + "/config/spreadsheet.json") as data:
        defaultWKS = json.load(data)["id"]

    def __init(self):
        return self
