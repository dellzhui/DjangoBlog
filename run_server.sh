#!/bin/sh

init_env()
{
    source /usr/local/virtualenvs/venv_devopspy/bin/activate
    sed -i 's/127.0.0.1/0.0.0.0/g' django/core/management/commands/runserver.py
}

init_server()
{
    pip install -t . -Ur requirements.txt
    ./manage.py makemigrations
    ./manage.py migrate
    sed -i 's/127.0.0.1/0.0.0.0/g' django/core/management/commands/runserver.py
}

run_server()
{
    ./manage.py runserver
}

init_env
[ "x$1" = "xinit" ] && init_server
run_server
