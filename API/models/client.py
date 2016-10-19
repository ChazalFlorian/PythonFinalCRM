from enum import Enum

class Client:
    name = String()
    entreprise = String()
    state = Enum('Prospect', 'Projet en cours', 'Projet Terminé', 'Partenaire')

    def init(self, name, entreprise, state):
        self.name = name
        self.entreprise = entreprise
        self.state = state

    def getName():
        return self.name

    def getEntreprise():
        return self.entreprise

    def getState():
        return self.state

    def setName(name):
        self.name = name

    def setEntreprise(entreprise):
        self.entreprise = entreprise

    def setState(state):
        self.state = state
