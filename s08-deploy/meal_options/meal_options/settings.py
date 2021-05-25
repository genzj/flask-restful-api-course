class Config(object):
    SECRET_KEY = 'secret key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./meal_options.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    ASSETS_DEBUG = True


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
