from functools import wraps

from flask import request, _request_ctx_stack, current_app
from flask_restful import abort
from werkzeug.local import LocalProxy


current_user = LocalProxy(lambda: _request_ctx_stack.top.user)


def login():
    _request_ctx_stack.top.user = None
    if 'USER_TOKEN' in request.headers and request.headers['USER_TOKEN'] == 'test-user':
        _request_ctx_stack.top.user = request.headers['USER_TOKEN']
        current_app.logger.info('user %s login', current_user)
        return True
    else:
        current_app.logger.warning('no user login')
        return False


def login_required(f):
    @wraps(f)
    def _f(*args, **kwargs):
        if not login():
            abort(401)
        return f(*args, **kwargs)
    return _f
 
