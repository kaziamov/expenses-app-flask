import psycopg2
from expenses_app.settings import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from psycopg2 import pool
from contextlib import contextmanager


def create_connection(*args, **kwargs):
    return psycopg2.connect(host=DB_HOST,
                            port=DB_PORT,
                            user=DB_USER,
                            password=DB_PASS,
                            database=DB_NAME)


def create_pool(min_conn=1, max_conn=5):
    """Create connection for work with PostgresSQL"""
    return pool.SimpleConnectionPool(minconn=min_conn,
                                     maxconn=max_conn,
                                     connection_factory=create_connection,
                                     host=DB_HOST,
                                     port=DB_PORT,
                                     user=DB_USER,
                                     password=DB_PASS,
                                     database=DB_NAME)


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
