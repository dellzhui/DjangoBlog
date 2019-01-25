#!/bin/sh


source /usr/local/virtualenvs/venv_devopspy/bin/activate

pip install -t . -Ur requirements.txt

sed -i 's/127.0.0.1/0.0.0.0/g' django/core/management/commands/runserver.py

./manage.py runserver


