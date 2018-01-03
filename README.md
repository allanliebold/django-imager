# django-imager

**Authors**: Darren Haynes & Allan Liebold

## Overview
A simple image management website using [Django](https://www.djangoproject.com/).

## Routes
| Route | Name | Description |
|:--|--|:--|
|`/`|home|the landing page|
|`/login`|login|GET: the login form page<br>POST: logs a user into their account, {username, password}|
|`/logout`|logout|log out the currently logged in user|
|`/profile/<username>`|profile|profile file for given user|
|`/profile/edit`|profile_edit| edit the current user's profile|
|`/images/library`|library|library of all the logged in user's albums and photos<br>GET: album_page: page number for albums, photo_page: page number for photos|
|`/images/photos/<id>`|photo_detail|detail of a single photo|
|`/images/albums/<id>`|album_detail|detail of a single album<br>GET: page: page number for photos in the album|
|`/images/photos/<id>/edit`|photo_edit|edit a single photo|
|`/images/albums/<id>/edit`|album_edit|edit a single album|
|`/images/photos/add`|photos_create|upload new pictures|
|`/images/albums/add`|photos_create|create new albums|
|`/accounts/*`|all registration routes| included from [django-registration](http://django-registration.readthedocs.io/en/stable/index.html)|
|`/admin/*`|all built-in admin routes| included from [Django admin](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#reversing-admin-urls)|

## Getting Started

Clone this repository to your local machine.
```
$ git clone https://github.com/allanliebold/django-imager.git
```

Once downloaded, change directory into the `django-imager` directory.
```
$ cd django-imager
```

Begin a new virtual environment with Python 3 and activate it.
```
django-imager $ python3 -m venv ENV
django-imager $ source ENV/bin/activate
```

Install the application requirements with [`pip`](https://pip.pypa.io/en/stable/installing/).
```
(ENV) django-imager $ pip install -r requirements.txt
```

Create a [Postgres](https://wiki.postgresql.org/wiki/Detailed_installation_guides) database for use with this application.
```
(ENV) django-imager $ createdb imager_db
```

Export environmental variables pointing to the location of database, your username, hashed password, and secret
```
(ENV) django-imager $ export SECRET_KEY='secret'
(ENV) django-imager $ export DB_NAME='imagersite'
(ENV) django-imager $ export DB_USER='(your postgresql username)'
(ENV) django-imager $ export DB_PASSWORD='(your postgresql password)'
(ENV) django-imager $ export DB_HOST='localhost'
(ENV) django-imager $ export DEBUG='True'
```

Then initialize the database with the `migrate` command from `manage.py`
```
(ENV) django-imager $ python imagersite/manage.py migrate
```

Once the package is installed and the database is created, start the server with the `runserver` command from `manage.py`
```
(ENV) django-imager $ python imagersite/manage.py runserver
```

Application is served on http://localhost:8000

## Testing
You can test this application by first exporting an environmental variable pointing to the location of a testing database, then running the `test` command from `manage.py`.
```
(ENV) django-imager $ export TEST_DB='imager_test'
(ENV) django-imager $ python imagersite/manage.py test imagersite
```