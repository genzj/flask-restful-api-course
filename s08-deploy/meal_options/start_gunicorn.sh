#!/bin/bash

gunicorn -c gunicorn.conf meal_options.wsgi
