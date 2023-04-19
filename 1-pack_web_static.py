#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date



def do_pack():
    time_string = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time_string))
        return ("versions/web_static_{}.tgz".format(time_string))
    except:
        return None

