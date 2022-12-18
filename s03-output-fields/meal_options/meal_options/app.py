from . import create_app
from .model import Option, Meal, TIME_FORMAT, list_of

import json

from datetime import datetime
from typing import List

from flask import request
from flask_restful import (
    Api,
    Resource,
    fields,
    marshal_with,
    marshal_with_field,
)

app = create_app()
api = Api(app)

meals: List[Meal] = []


def create_meal(meal_time):
    idx = len(meals)
    meal = Meal(idx, datetime.strptime(meal_time, TIME_FORMAT))
    meals.append(meal)
    return meal


def create_option(meal_id, place):
    meal = meals[meal_id]
    options = meal.options
    idx = len(options)
    option = Option(idx, place)
    options.append(option)
    return option


class Meals(Resource):
    @marshal_with_field(list_of(Meal))
    def get(self):
        return meals

    @marshal_with(Meal.fields)
    def post(self):
        data = json.loads(request.data)
        return create_meal(data['meal_time'])


api.add_resource(Meals, '/meals')


class Options(Resource):
    @marshal_with_field(list_of(Option))
    def get(self, meal_id):
        return meals[meal_id].options

    @marshal_with(Option.fields)
    def post(self, meal_id):
        data = json.loads(request.data)
        return create_option(meal_id, data['place'])


api.add_resource(Options, '/meals/<int:meal_id>/options')


class Votes(Resource):
    @marshal_with_field(fields.Integer)
    def post(self, meal_id, option_id):
        meals[meal_id].options[option_id].votes += 1
        return meals[meal_id].options[option_id].votes


api.add_resource(Votes, '/meals/<int:meal_id>/options/<int:option_id>/votes')
