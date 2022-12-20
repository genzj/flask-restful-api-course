from .model import db
from pathlib import Path
import logging.config

from flask import Flask


def configure_logging():
    logging.config.dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s", # noqa
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "formatter": "default",
                }
            },
            "root": {"level": "INFO", "handlers": ["wsgi"]},
            # "loggers": {
            #     "sqlalchemy.engine": {"level": "INFO"},
            # },
        }
    )


def create_app(config_overrides=None):
    configure_logging()  # should be configured before any access to app.logger
    app = Flask(__name__)
    app.config.from_object("meal_options.default_settings")
    app.config.from_prefixed_env()

    if config_overrides is not None:
        app.config.from_mapping(config_overrides)

    db.init_app(app)
    db_file = Path(app.config['SQLALCHEMY_DATABASE_URI'].strip('sqlite:///'))
    if not db_file.exists():
        print(f'creating database ${db_file}')
        with app.app_context():
            db.create_all()

    return app
