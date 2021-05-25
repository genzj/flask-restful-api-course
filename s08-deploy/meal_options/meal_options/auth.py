from flask import request, current_app, _request_ctx_stack
from flask_restful import abort
from werkzeug.local import LocalProxy

current_user = LocalProxy(lambda: _request_ctx_stack.top.user)


def login():
    if 'USER_TOKEN' in request.headers and \
            request.headers['USER_TOKEN'] == 'test-user':
        _request_ctx_stack.top.user = 'test'
        current_app.logger.info('user %s login', current_user)
    else:
        current_app.logger.warning('no user login')
        _request_ctx_stack.top.user = None

    return _request_ctx_stack.top.user is not None


def login_required(f):

    def _wrapped(*args, **kwargs):
        if not login():
            abort(401)
        return f(*args, **kwargs)

    return _wrapped
