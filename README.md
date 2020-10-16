# NewsNaathProj

docker-compose run --rm newsnaath python manage.py createsuperuser
docker-compose run --rm newsnaath python manage.py makemigrations
docker-compose run --rm newsnaath python manage.py migrate
docker-compose run --rm newsnaath python manage.py test

# Debugging
