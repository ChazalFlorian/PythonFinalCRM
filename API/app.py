import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)

from API import app
from API.models.clients import Clients

if __name__ == '__main__':
    app.run()

client = Clients()
