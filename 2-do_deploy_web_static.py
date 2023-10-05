#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers
using the function deploy
"""
from fabric.api import env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['52.3.250.55', '54.89.107.230']
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Uncompress the archive to the folder /data/web_static
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, name))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(filename))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))

        print("New version deployed!")

        return True

    except Exception:
        return False
