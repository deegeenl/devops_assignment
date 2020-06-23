# Simple Birthday API app

## What it does

1. Description: Saves/updates the given user's name and date of birth in the database

    **Request**: `PUT /hello/Morty { "dateOfBirth": "2000-01-01" }`

    **Response**: 204 No Content

2. Description: Return a hello/birthday message for the given user

    **Request**: GET /hello/Morty

    **Response**: 200 OK with the following content:
    
    a. when Morty’s birthday is in 5 days:
        `{"message": "Hello, Morty! Your birthday is in 5 days"}`

    b. when Morty's birthday is today:
        `{"message": "Hello, Morty! Happy birthday"}`

## Run the project

### Requirements:

- Install python 3.8 (with apt-get on debian/ubuntu or with [installer package for MacOS](https://www.python.org/downloads/mac-osx/))
- Install postgresql (with apt-get or brew on MacOS)

### Setup postgresql:

In a shell:
```buildoutcfg
createuser birthday
createdb birthday_db
psql -d birthday_db
```

Then in the `psql` console:
```sql
alter user birthday with encrypted password 'birthday';
grant all privileges on database birthday_db to birthday;
alter user birthday createdb;
```

### Create virtual environment:

Clone the project with git, then inside the project:
```sh
python3 -m venv venv  # or python
echo venv/ >> .gitignore
source venv/bin/activate
pip install -r requirements.txt
```

### Run the project in localhost:

```buildoutcfg
./manage.py migrate
./manage.py test  # run the tests
./manage.py runserver  # run a dev server
```
The tests should pass (6 tests). After running runserver, you should be able to use Postman to
test the app by going to http://127.0.0.1:8000/ and hitting the `/hello/<name>` url.

If you want to use the Django admin, create a superuser first:
```buildoutcfg
./manage.py createsuperuser --username <your_name> --email <you@example.com>
```
You will be prompted to specify a password.

Now you can go to http://127.0.0.1:8000/admin to use the admin panel.

### Run the project with gunicorn:

gunicorn is a python WSGI server that was installed with `pip install` above.

On a linux machine, you can run (inside the project directory):
```buildoutcfg
gunicorn birthday.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3
``` 
to bind the app to port 8010 on localhost, for example.

(On a Mac, you'll need to change the user, `www-data` doesn't exist by default). 
