#!/usr/bin/python3
"""
this Script generates a .tgz archive from the contents
of the web_static folder
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    create a file .tgz
    """
    try:
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_{}.tgz".format(date_time)
        local("mkdir -p versions")
        print("Packing web_static to {}".format(file))
        local("tar -czvf {} web_static".format(file))
    except:
        None
