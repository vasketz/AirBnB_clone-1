#!/usr/bin/python3
"""
this Script generates a .tgz archive from the contents
of the web_static folder
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    try:
        local("mkdir -p versions")
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_{}.tgz".format(date_time)
        local("tar -czvf {} web_static".format(file))
        return file
    except:
        return
