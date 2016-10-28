from API.models.client import Client


class Clients:

    __instance = None

    class __Clients:

        def __init__(self):
            self.container = []
            self.lastId = 0

        def addClient(self, name, entreprise, state):
                client = Client(self.lastId + 1, name, entreprise, state)
                self.container.append(client)
                self.lastId += 1
                return client

    def __init__(self):
        if not Clients.__instance:
            Clients.__instance = Clients.__Clients()

    def __getattr__(self, name):
        return getattr(self.__instance, name)
