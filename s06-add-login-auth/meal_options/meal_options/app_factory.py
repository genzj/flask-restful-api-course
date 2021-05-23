from pathlib import Path

from flask import Flask

from .model import db


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

    db.init_app(app)
    db_file = Path(app.config['SQLALCHEMY_DATABASE_URI'].strip('sqlite:///'))
    if not db_file.exists():
        print(f'creating database ${db_file}')
        db.create_all(app=app)

    # if app.config['DEBUG']:
    #     import logging
    #     logging.basicConfig()
    #     logger = logging.getLogger('sqlalchemy.engine')
    #     logger.setLevel(logging.INFO)

    return app
