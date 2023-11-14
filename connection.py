import psycopg2
from config import config


def connect():
    conn = None
    try:
        params = config(section='postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print('Connecting to the PostgreSQL Database...')
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn


def close(conn: psycopg2.extensions.connection):
    conn.close()
    print('Database connection closed.')
