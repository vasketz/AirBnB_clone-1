#!/usr/bin/python3
"""
this Script generates a .tgz archive from the contents
of the web_static folder
"""


from fabric.api import *
from os import path


env.user = 'ubuntu'
env.hosts = ['34.74.231.67', '54.172.241.181']


def do_deploy(archive_path):
    """
    descompress tar, deploy on servers
    """
    if path.exists(archive_path) is False:
        return False

    put(archive_path, "/tmp/")
    file = archive_path.replace(".tgz", "")
    file = file.replace("versions/", "")
    run("mkdir -p /data/web_static/releases/{}/".format(file))
    run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(
        file, file))
    run("rm /tmp/{}.tgz".format(file))
    run("mv /data/web_static/releases/{}/web_static/* ".format(
        file) + "/data/web_static/releases/{}/".format(file))
    run("rm -rf /data/web_static/releases/{}/web_static".format(file))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
        file))
    print("New version deployed!")
    return True
