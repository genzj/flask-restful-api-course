from flask import request, current_app, g
from flask_restful import abort


def login():
    if 'USER_TOKEN' in request.headers and \
            request.headers['USER_TOKEN'] == 'test-user':
        g.current_user = 'test'
        current_app.logger.info('user %s login', g.current_user)
    else:
        current_app.logger.warning('no user login')
        g.current_user = None

    return g.current_user is not None


def login_required(f):

    def _wrapped(*args, **kwargs):
        if not login():
            abort(401)
        return f(*args, **kwargs)

    return _wrapped
