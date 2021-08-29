#!/usr/bin/python3
"""
this Script generates a .tgz archive from the contents
of the web_static folder
"""


from fabric.api import *
from datetime import datetime
from os import path


env.user = 'ubuntu'
env.hosts = ['34.74.231.67', '54.172.241.181']


def do_pack():
    """
    create a file .tgz
    """
    try:
        local("mkdir -p versions")
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_{}.tgz".format(date_time)
        local("tar -czvf {} web_static".format(file))
        return file
    except:
        return None


def do_deploy(archive_path):
    """
    descompress tar
    """
    if path.exists(archive_path) is False:
        return False
    file = archive_path.split("/")[1]
    path_folder = file[:-4]

    put(archive_path, "/tmp/")
    run("mkdir -p /data/web_static/releases/{}/".format(path_folder))
    run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}".format(
        file, path_folder))
    run("rm -r /tmp/{}".format(file))
    run("mv /data/web_static/releases/{}/web_static/* ".format(
        path_folder) + "/data/web_static/releases/{}".format(path_folder))
    run("rm -rf /data/web_static/releases/{}/web_static".format(path_folder))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{} /data/web_static/current/".format(
        path_folder))
    print("New version deployed!")
    return True
