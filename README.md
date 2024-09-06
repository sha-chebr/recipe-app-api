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

#10 makemigrations:
docker-compose run --rm app sh -c "python manage.py makemigrations"

#11 migrate:
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
    - this will raise "django.db.migrations.exceptions.InconsistentMigrationHistory" exception
    - follow the steps below to resolve.
        1. run "docker volume ls"
        2. get the database volume (in our case it is "recipe-app-api-dev-db-data")
        3. remove the volume. run "docker volume rm recipe-app-api_dev-db-data" (make sure the docker-compose down command is run first)
        4. Now run #11 migrate command

#12 create superuser:
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py createsuperuser"
Email: admin@example.com
Password: admin

User One:
user@example.com
userone1

#13 Create user app
docker-compose run --rm app sh -c "python manage.py startapp user"

#14 User Two
Awesome!23 436625ccd30ca28d68ad9c23e1871dfbad8e7938

#15 create another django-project called "recipe":
docker-compose run --rm app sh -c "python manage.py startapp recipe"