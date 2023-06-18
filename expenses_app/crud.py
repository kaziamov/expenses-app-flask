import datetime

now = datetime.datetime.now


def _create_tables(conn):
    with conn.cursor() as cursor:
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


def add_category(conn, data):
    with conn.cursor() as cursor:
        cursor.execute("""INSERT INTO categories (name) VALUES (%s) ;""", (data, ))


def add_currency(conn, name):
    with conn.cursor() as cursor:
        cursor.execute("""INSERT INTO currencies (name) VALUES (%s) ;""", (name,))


def add_new_expence(conn, data):
    with conn.cursor() as cursor:
        cursor.execute("""INSERT INTO expenses (name, sum, date, currency, category)
                       VALUES (%s, %s, %s, %s, %s) ;""", data)


def get_data(conn, table):
    with conn.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM {table}""")
        return cursor.fetchall()


def get_categories(conn):
    return get_data(conn, 'categories')


def get_currencies(conn):
    return get_data(conn, 'currencies')


def get_expenses(conn):
    return get_data(conn, 'expenses')
