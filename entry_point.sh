cd src
# python manage.py shell < init_admin.py
python manage.py makemigrations
python manage.py migrate

echo 'Django is migrated with tables and relations'
python manage.py runserver