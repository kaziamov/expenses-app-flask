import psycopg2

import datetime
from expenses_app.settings import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

now = datetime.datetime.now

def make_connection():
    return psycopg2.connect(host=DB_HOST,
                            port=DB_PORT,
                            user=DB_USER,
                            password=DB_PASS,
                            database=DB_NAME)


def __create_tables():
    c = make_connection()
    cursor = c.cursor()
    cursor.execute("""CREATE TABLE categories (
        id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        name varchar(255),
        created_at DATE );""")
    cursor.execute("""CREATE TABLE currencies (
        id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        name varchar(255),
        created_at DATE );""")
    cursor.execute("""CREATE TABLE expenses (
        id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        name varchar(255),
        sum FLOAT,
        currency BIGINT REFERENCES categories (id),
        date DATE,
        category BIGINT REFERENCES categories (id),
        created_at DATE );""")
    c.commit()
    c.close()


def create_category(data):
    c = make_connection()
    cursor = c.cursor()
    cursor.execute("""INSERT INTO categories (name)
                   VALUES (%s) ;""", data)
    c.commit()
    c.close()


def create_currency(name):
    c = make_connection()
    cursor = c.cursor()
    cursor.execute("""INSERT INTO currencies (name)
                   VALUES (%s) ;""", (name, now()))
    c.commit()
    c.close()


def add_new_expence(data):
    c = make_connection()
    cursor = c.cursor()
    cursor.execute("""INSERT INTO expenses (name, sum, date, currency, category, is_income)
                   VALUES (%s, %s, %s, %s, %s, %s) ;""", data)
    c.commit()
    c.close()