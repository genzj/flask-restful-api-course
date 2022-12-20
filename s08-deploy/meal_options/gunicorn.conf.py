worker_class = 'gevent'
workers = 2
bind = '127.0.0.1:5000'

access_logfile = '-'
error_logfile = '-'
log_level = 'debug'

chdir = 'meal_options'

wsgi_app = 'meal_options.wsgi'
