release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
web: gunicorn universo_nextlevel.wsgi --log-file -
