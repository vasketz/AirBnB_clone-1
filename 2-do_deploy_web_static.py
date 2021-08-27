#!/usr/bin/python3
"""
this Script generates a .tgz archive from the contents
of the web_static folder
"""


from fabric.api import *
from datetime import datetime
from os import path


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
    else:
        return None


def do_deploy(archive_path):
    """
    descompress tar
    """
    if path.exist(archive_path) is False:
        return False
    file = archive_path.split("/")

    put(archive_path, "/tmp/")
