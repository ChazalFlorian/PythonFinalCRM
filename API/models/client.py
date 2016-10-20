from enum import Enum


class Client:
    state = Enum('Prospect', 'Projet en cours', 'Projet Terminé', 'Partenaire')

    def init(self, name, entreprise, state):
        self.name = name
        self.entreprise = entreprise
