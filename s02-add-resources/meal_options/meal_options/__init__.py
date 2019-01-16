from .app_factory import create_app
from flask_restful import Api


app = create_app('meal_options.settings.DevConfig')
api = Api(app)

from . import views

