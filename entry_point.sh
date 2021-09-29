#!/bin/sh
python manage.py shell
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

echo 'Django is migrated with tables and relations'
python manage.py runserver 0.0.0.0:8000