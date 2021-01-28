release: python manage.py makemigrations pet_shelter
release: python manage.py migrate
release: python manage.py loaddata shelter_data.json
web: gunicorn shelter.wsgi