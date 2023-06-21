import psycopg2
from .settings import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, MAX_CONN, MIN_CONN
from psycopg2 import pool
from contextlib import contextmanager


def create_connection(*args, **kwargs):
    """Create connection for work with PostgresSQL"""
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )


def create_pool():
    """Create pool of connections for work with PostgresSQL"""
    return pool.SimpleConnectionPool(
        minconn=MIN_CONN,
        maxconn=MAX_CONN,
        connection_factory=create_connection,
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )


@contextmanager
def get_connection():
    """Get connection from pool or error if connection doesn't work"""
    conn = None
    try:
        conn = conn_pool.getconn()
        yield conn
        conn.commit()
    except Exception as error:
        conn.rollback()
        raise Exception(f'Connection lost. Changes abort. {error}')
    finally:
        if conn:
            conn_pool.putconn(conn)


conn_pool = create_pool()
