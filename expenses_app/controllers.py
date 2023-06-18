from .db_connect import get_connection
from .crud import add_category, add_currency


def add_new_currency(data):
    new_currency = data["new_currency"].strip()
    with get_connection() as conn:
        add_currency(conn, new_currency)
    return new_currency


def add_new_category(data):
    with get_connection() as conn:
        new_category = data["new_category"].strip()
        add_category(conn, new_category)
    return new_category
