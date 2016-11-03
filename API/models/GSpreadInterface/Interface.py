import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials


class GSpreadInterface():

    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        sys.path[0] + "/config/config.json",
        scope
        )
    gc = gspread.authorize(credentials)

    def __init(self):
        print (self)
        return self
