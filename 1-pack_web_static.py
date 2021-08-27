#!/usr/bin/python3
"""
this Script generates a .tgz archive from the contents
of the web_static folder
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    local("mkdir -p versions")
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file = local("tar -cvzf versions/web_static_{}.tgz ./web_static".format(
                 now), capture=True)
    if file.succeeded:
        return ("versions/web_static_{}.tgz".format(now))
    else:
        return None
