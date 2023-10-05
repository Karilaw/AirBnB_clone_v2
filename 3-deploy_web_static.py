#!/usr/bin/python3
""" creates and distributes an archive to your web servers"""
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists

env.hosts = ['52.3.250.55', '54.89.107.230']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    file_name = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S")
    )
    result = local("tar -cvzf {} web_static".format(file_name))
    return file_name if result.succeeded else None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, name))
        run("rm /tmp/{}".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))

        print("New version deployed!")

        return True

    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to your web servers
    """
    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
