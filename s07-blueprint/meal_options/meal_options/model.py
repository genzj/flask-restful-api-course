from flask_restful import fields
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def list_of(cls):
    return fields.List(fields.Nested(cls.fields))


class Option(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.Unicode(256), nullable=False)
    votes = db.Column(db.Integer, default=0)

    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'))

    fields = {
        'id': fields.Integer,
        'place': fields.String,
        'votes': fields.Integer,
    }


class Meal(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(
        db.DateTime(timezone=False), nullable=False, default=datetime.utcnow
    )
    meal_time = db.Column(db.DateTime(timezone=False), nullable=False)

    options = db.relationship("Option", backref="meal")

    fields = {
        'id': fields.Integer,
        'create_time': fields.DateTime,
        'meal_time': fields.DateTime,
        'options': list_of(Option),
    }
