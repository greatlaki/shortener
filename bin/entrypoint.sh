#!/bin/bash

set -e

GUNICORN_TIMEOUT=${GUNICORN_TIMEOUT:-600}
GUNICORN_WORKERS=${GUNICORN_WORKERS:-2}

python manage.py migrate
python manage.py runserver

gunicorn --bind 0.0.0.0:8000 src.wsgi --workers $GUNICORN_WORKERS --timeout $GUNICORN_TIMEOUT