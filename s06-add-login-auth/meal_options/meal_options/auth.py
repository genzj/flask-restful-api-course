from flask import request, current_app


def login():
    if 'USER_TOKEN' in request.headers and \
            request.headers['USER_TOKEN'] == 'test-user':
        current_user = 'test'
        current_app.logger.info('user %s login', current_user)
    else:
        current_app.logger.warning('no user login')
        current_user = None
    return current_user
