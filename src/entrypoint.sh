#!/bin/bash

pipenv run python example/manage.py migrate
pipenv run python example/manage.py collectstatic --noinput
pipenv run python example/manage.py runserver 0.0.0.0:8000
