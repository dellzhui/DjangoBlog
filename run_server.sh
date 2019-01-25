#!/bin/sh


source /usr/local/virtualenvs/venv_devopspy/bin/activate

sed -i 's/127.0.0.1/0.0.0.0/g' django/core/management/commands/runserver.py

./manage.py runserver
if [ $? -ne 0 ];then
    pip install -t . -Ur requirements.txt
    ./manage.py runserver
fi
