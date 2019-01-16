import json

from datetime import datetime

from flask import request
from flask_restful import Resource, marshal_with, marshal_with_field, reqparse

from . import app, api
from .model import Option, Meal, TIME_FORMAT, list_of


def parse_datetime(s):
    return datetime.strptime(s, TIME_FORMAT)


meal_args = reqparse.RequestParser()
meal_args.add_argument('meal_time', required=True, type=parse_datetime, help='time of the meal in format ' + TIME_FORMAT)

option_args = reqparse.RequestParser()
option_args.add_argument('place', required=True, type=str, help='place for of the meal')


meals = []


def create_meal(meal_time):
    idx = len(meals)
    meal = Meal(idx, meal_time)
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
        args = meal_args.parse_args()
        return create_meal(args['meal_time'])


api.add_resource(Meals, '/meals')


class Options(Resource):
    @marshal_with_field(list_of(Option))
    def get(self, meal_id):
        return meals[meal_id].options

    @marshal_with(Option.fields)
    def post(self, meal_id):
        args = option_args.parse_args()
        return create_option(meal_id, args['place'])


api.add_resource(Options, '/meals/<int:meal_id>/options')


class Votes(Resource):
    def post(self, meal_id, option_id):
        meals[meal_id].options[option_id].votes += 1
        return 'OK'


api.add_resource(Votes, '/meals/<int:meal_id>/options/<int:option_id>/votes')

