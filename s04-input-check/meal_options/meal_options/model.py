from flask_restful import fields
from datetime import datetime

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def list_of(cls):
    return fields.List(fields.Nested(cls.fields))


class Option(object):
    fields = {
        'id': fields.Integer,
        'place': fields.String,
        'votes': fields.Integer,
    }

    def __init__(self, idx, place):
        self.id = idx
        self.place = place
        self.votes = 0


class Meal(object):
    fields = {
        'id': fields.Integer,
        'create_time': fields.DateTime,
        'meal_time': fields.DateTime,
        'options': list_of(Option),
    }

    def __init__(self, idx, meal_time):
        self.id = idx
        self.create_time = datetime.utcnow()
        self.meal_time = meal_time
        self.options = []
