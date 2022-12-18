from flask import request, current_app
from flask_restful import abort


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
