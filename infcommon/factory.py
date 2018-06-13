# -*- coding: utf-8 -*-

import os

from infcommon import mysql

class Factory(object):
    _instances = {}

    @classmethod
    def instance(cls, id, create_instance):
        if id not in cls._instances:
            cls._instances[id] = create_instance()

        return cls._instances[id]

def mysql_client(db_uri=None):
    if db_uri is None:
        db_uri = os.getenv("LOCAL_DB_URI")

    return Factory.instance('mysql_client_{}'.format(db_uri),
                            lambda: mysql.MySQLClient(db_uri))
