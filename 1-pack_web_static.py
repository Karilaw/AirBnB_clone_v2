#!/usr/bin/env python3
"""
This script generates a .tgz archive from the
contents of the web_static folder
"""
from fabric import Connection, Config
from datetime import datetime
import os


class Fabfile(object):
    """
    A class used to represent a Fabric file

    ...

    Attributes
    ----------
    conn : Connection
        a Fabric Connection object that represents a shell session

    Methods
    -------
    do_pack()
        Generates a .tgz archive from the contents of the web_static folder
    """

    def __init__(self, connection):
        """
        Parameters
        ----------
        connection : Connection
            a Fabric Connection object that represents a shell session
        """

        self.conn = connection

    def do_pack(self):
        """
        Generates a .tgz archive from the contents of the web_static folder
        Returns
        -------
        str
            a string which is the path of the .tgz file if successful, otherwise None
        """

        # Create the versions directory if it doesn't exist
        self.conn.local("mkdir -p versions")

        # Create a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(timestamp)

        # Use the tar command to create a tar gzipped archive of the web_static directory
        result = self.conn.local("tar -cvzf {} web_static".format(filename))

        # If the command was successful, return the name of the file. Otherwise, return None.
        if result.ok:
            return filename
        else:
            return None
