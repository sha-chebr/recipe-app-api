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

#7 create another django-project called "core":
docker-compose run --rm app sh -c "python manage.py startapp core"

#8 After adding core app and test for wait_for_db:
docker-compose run --rm app sh -c "python manage.py test"

#9 wait_for_db:
docker-compose run --rm app sh -c "python manage.py wait_for_db"