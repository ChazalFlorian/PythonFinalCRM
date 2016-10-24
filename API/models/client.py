from enum import Enum


State = Enum(
    'State',
    [
        ('prospect', 'Prospect'),
        ('inProgress', 'Projet en cours'),
        ('finished', 'Projet terminé'),
        ('partner', 'Partenaire')
    ]
)


class Client:

    def __init__(self, id, name, company, state):
        self.id = id
        self.name = name
        self.company = company
        self.state = State[state]
