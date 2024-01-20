commands (run from the project directory):


#1
docker-compose build

#2 linting
docker-compose run --rm app sh -c "flake8"

#3 Unit Tests
docker-compose run --rm app sh -c "python manage.py test"