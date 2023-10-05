#!/usr/bin/python3
""" deletes out-of-date archives, using the function do_clean"""
from fabric.api import env, local, run
from os.path import exists
env.hosts = ['52.3.250.55', '54.89.107.230']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)

    # Keep at least one archive if number is less than 1
    if number < 1:
        number = 1

    # Delete archives in versions folder
    local('ls -t versions | tail -n +{} | xargs rm -f --'.format(number + 1))

    # Delete archives in /data/web_static/releases folder of web servers
    run('ls -t /data/web_static/releases | tail -n +{} | xargs rm -rf --'.format(number + 1))
