#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=apps.settings.production

echo 'Applying migrations...'
python manage.py wait_for_db --settings=apps.settings.production
python manage.py migrate --settings=apps.settings.production

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=apps.settings.production apps.wsgi:application --bind 0.0.0.0:8000