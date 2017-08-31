# Setup
Use instructions from here to set up a virtual environment: https://docs.djangoproject.com/en/1.11/intro/contributing/#getting-a-copy-of-django-s-development-version

Steps for windows:

```
pip install virtualenvwrapper
mkvirtualenv gcmwapp
workon gcmwapp
``` 

Then set up requirements:
`pip install -r requirements.txt`

Each time you open this command prompt window, you have to type `workon gcmwapp` before doing anything.

## DB migration
Run this; also run these commands whenever you make changes to your models.
```
python manage.py makemigrations
python manage.py migrate
```

To set up initial data when you're just starting, load them from fixtures like this:
```
python manage.py loaddata gcmw/fixtures/main.json
```

## Edit hosts file
```
cd C:\Windows\System32\drivers\etc
explorer .
```
Or 
```vim C:\Windows\System32\drivers\etc\hosts```

Add this line:
```
127.0.0.1       localhost
```


## Running the server
`python manage.py runserver`

Open localhost:8000 in your browser.
Subdomains should be like alpharetta.localhost:8000, etc.

# Initial setup (for ashwin)
# Requirements.txt
When you install a new package:
`pip freeze > requirements.txt`

# Dump date
To dump local data periodically:
`python manage.py dumpdata --natural-primary --indent 1 -o gcmw/fixtures/main.json`

# Start
```
django-admin startproject gcmw
python manage.py startapp acharyas
```

# User (for admin)
```
python manage.py createsuperuser
```

# Other commands
`python manage.py shell`
`python manage.py dbshell`