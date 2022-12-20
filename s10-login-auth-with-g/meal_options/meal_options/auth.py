from functools import wraps
from flask import request, current_app, g
from flask_restful import abort
from werkzeug.local import LocalProxy


def login():
    token_map = current_app.config.get('TOKEN_TO_USER_MAPPING', dict())
    if 'USER_TOKEN' in request.headers:
        current_user = token_map.get(request.headers['USER_TOKEN'], None)
    else:
        current_user = None

    if current_user:
        current_app.logger.info('user %s login', current_user)
    else:
        current_app.logger.warning('no user login')
        abort(403)
    return current_user


def get_current_user_from_g() -> str:
    if 'current_user' not in g:
        g.current_user = login()
    return g.current_user


current_user = LocalProxy(get_current_user_from_g)


def login_required(f):
    @wraps(f)
    def _wrapped(*args, **kwargs):
        get_current_user_from_g()
        return f(*args, **kwargs)

    return _wrapped
