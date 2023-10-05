#!/usr/bin/env python3
"""
This script generates a .tgz archive from the
contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """

    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Create a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(timestamp)

    # Use the tar command to create a .tgz archive of the web_static directory
    result = local("tar -cvzf {} web_static".format(filename))

    # If the command was successful, return the name of the file. Otherwise, return None.
    if result.succeeded:
        return filename
    else:
        return None
