#!/bin/sh

cd djangobackend
python manage.py shell
python manage.py makemigrations
python manage.py migrate

echo 'Django is migrated with tables and relations'
python manage.py runserver 0.0.0.0:8000