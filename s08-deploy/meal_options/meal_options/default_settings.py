DEBUG = False  # make sure DEBUG is off unless enabled explicitly otherwise
SQLALCHEMY_DATABASE_URI = 'sqlite:///./meal_options.db'
TOKEN_TO_USER_MAPPING = {
    # token    : username
    'test-user': 'test',
}
