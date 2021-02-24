import pytest
from django.db import connections

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def run_sql(sql):
    conn = psycopg2.connect(
        database="test_postgres",
        user="postgres",
        host="localhost",
        password="dbpass"
    )

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()


# @pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings

    # settings.DATABASES['default']['NAME'] = 'db'

    # run_sql('DROP SCHEMA IF EXISTS test_schema')
    # run_sql('CREATE SCHEMA IF NOT EXISTS test_schema')

    yield

    for connection in connections.all():
        connection.close()

    # run_sql('DROP SCHEMA IF EXISTS test_schema')
