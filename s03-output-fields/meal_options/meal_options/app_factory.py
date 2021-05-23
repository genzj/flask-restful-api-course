from flask import Flask


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    Arguments:
        object_name: the python path of the config object,
                     e.g. meal_options.settings.ProdConfig
    """

    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config.from_envvar('MEAL_OPTIONS_SETTINGS', silent=True)

    return app
