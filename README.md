commands (run from the project directory):


#1 :
docker-compose build

#2 linting:
docker-compose run --rm app sh -c "flake8"

#3 Unit Tests:
docker-compose run --rm app sh -c "python manage.py test"

#4 flake8:
docker-compose run --rm app sh -c "flake8"

#5 django-project:
docker-compose run --rm app sh -c "django-admin startproject app ."

#6 startup your project:
docker-compose up