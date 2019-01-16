import json

from datetime import datetime

from flask import request, Blueprint
from flask_restful import Api, Resource, marshal_with, marshal_with_field, reqparse

from .model import Option, Meal, TIME_FORMAT, list_of, db
from .auth import login_required, current_user


def parse_datetime(s):
    return datetime.strptime(s, TIME_FORMAT)


meal_args = reqparse.RequestParser()
meal_args.add_argument('meal_time', required=True, type=parse_datetime, help='time of the meal in format ' + TIME_FORMAT)

option_args = reqparse.RequestParser()
option_args.add_argument('place', required=True, type=str, help='place for of the meal')


meal_options_blueprint = Blueprint('meal_option', __name__)
api = Api(meal_options_blueprint)


def create_meal(meal_time):
    meal = Meal(meal_time=meal_time)
    db.session.add(meal)
    db.session.commit()
    return meal


def create_option(meal_id, place):
    meal = Meal.query.get_or_404(meal_id)
    option = Option(place=place)
    meal.options.append(option)
    db.session.commit()
    return option



class Meals(Resource):
    @marshal_with_field(list_of(Meal))
    @login_required
    def get(self):
        print('---->', 'current user is:', current_user)
        return Meal.query.all()

    @marshal_with(Meal.fields)
    def post(self):
        args = meal_args.parse_args()
        return create_meal(args['meal_time'])


api.add_resource(Meals, '/meals')


class Options(Resource):
    @marshal_with_field(list_of(Option))
    def get(self, meal_id):
        meal = Meal.query.get_or_404(meal_id)
        # return Option.query.with_parent(meal).all()
        return meal.options

    @marshal_with(Option.fields)
    def post(self, meal_id):
        args = option_args.parse_args()
        return create_option(meal_id, args['place'])


api.add_resource(Options, '/meals/<int:meal_id>/options')


class Votes(Resource):
    def post(self, meal_id, option_id):
        meal = Meal.query.get_or_404(meal_id)
        option = Option.query.with_parent(meal).filter(Option.id == option_id).first_or_404()
        print('----->', str(Option.query.with_parent(meal)))
        # option.votes += 1
        option.votes = Option.votes + 1
        db.session.commit()
        return 'OK'


api.add_resource(Votes, '/meals/<int:meal_id>/options/<int:option_id>/votes')

