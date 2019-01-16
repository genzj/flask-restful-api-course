class Config(object):
    SECRET_KEY = 'secret key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1:3306/test'
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

