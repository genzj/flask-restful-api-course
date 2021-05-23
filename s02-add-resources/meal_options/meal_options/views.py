import json

from datetime import datetime
from typing import List

from flask import request
from flask_restful import Resource

from meal_options import api

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

meals: List[dict] = []


def datetime_format(dt):
    return dt.strftime(TIME_FORMAT)


def create_meal(meal_time):
    idx = len(meals)
    meal = {
        'id':
            idx,
        'create_time':
            datetime_format(datetime.utcnow()),
        'meal_time':
            datetime_format(datetime.strptime(meal_time, TIME_FORMAT)),
        'options': [],
    }
    meals.append(meal)
    return meal


def create_option(meal_id, place):
    meal = meals[meal_id]
    options = meal['options']
    idx = len(options)
    option = {
        'id': idx,
        'place': place,
        'votes': 0,
    }
    options.append(option)
    return option


class Meals(Resource):

    def get(self):
        return meals

    def post(self):
        data = json.loads(request.data)
        return create_meal(data['meal_time'])


api.add_resource(Meals, '/meals')


class Options(Resource):

    def get(self, meal_id):
        return meals[meal_id]['options']

    def post(self, meal_id):
        data = json.loads(request.data)
        return create_option(meal_id, data['place'])


api.add_resource(Options, '/meals/<int:meal_id>/options')


class Votes(Resource):

    def post(self, meal_id, option_id):
        meals[meal_id]['options'][option_id]['votes'] += 1
        return str(meals[meal_id]['options'][option_id]['votes'])


api.add_resource(Votes, '/meals/<int:meal_id>/options/<int:option_id>/votes')
