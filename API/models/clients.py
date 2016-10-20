from API.models import Client


class Clients:

    def init():
        self.Contener = []

    def addClient(firstname, entreprise, state):
            test = Client(firstname, entreprise, state)
            self.Contener.append(test)
            return test
