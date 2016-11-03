from enum import Enum
from API import db


State = Enum(
    'State',
    [
        ('prospect', 'Prospect'),
        ('inProgress', 'Projet en cours'),
        ('finished', 'Projet terminé'),
        ('partner', 'Partenaire')
    ]
)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    company = db.Column(db.String(80))
    state = db.Column(db.Enum(State))

    def __init__(self, name, company, state):
        self.name = name
        self.company = company
        self.state = state

    def __repr__(self):
        return '<User %r>' % self.name
