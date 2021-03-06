# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras
from six.moves.urllib.parse import urlparse

def connect(uri):
    result = urlparse(uri)
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname

    if result.scheme == 'postgres' or result.scheme == 'postgresql':
        return connect_psycopg2(
                database=database,
                user=username,
                password=password,
                host=hostname)

    return None

def connect_psycopg2(*args, **kwargs):
    db = psycopg2.connect(*args, **kwargs)

    db.cursor_factory = psycopg2.extras.DictCursor

    return db
