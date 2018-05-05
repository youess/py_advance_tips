# -*- coding: utf-8 -*-

import db_connection


# in dev_main.py or set the same parameter to specify the option
TESTING = True
db = db_connection.Database()

# in prod_main.py
TESTING = False
db = db_connection.Database()


# db_connection.py
class TestDatabase(object):
    pass


class RealDatabase(object):
    pass


if TESTING:
    Database = TestDatabase
else:
    Database = RealDatabase
