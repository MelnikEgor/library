python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
cp -r /app/collected_static/. /backend_static/static/
gunicorn --bind 0.0.0.0:8000 backend.wsgi