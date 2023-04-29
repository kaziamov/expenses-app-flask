from flask import render_template, request, flash, redirect, url_for, Blueprint
from expenses_app.models import (add_currency,
                                 add_category,
                                 add_new_expence,
                                 get_categories,
                                 get_currencies,
                                 get_expenses)
from expenses_app.db_connect import get_connection


main = Blueprint('main', __name__)


@main.route('/', methods=["GET"])
def root():
    return redirect(url_for('main.expenses'))


@main.route('/add_new_expense', methods=["POST"])
def add_new_expense():
    with get_connection() as conn:
        form_values = request.form.to_dict()
        data = (form_values['name'],
                form_values["sum"],
                form_values["date"],
                form_values['currency'],
                form_values["category"],
                )
        add_new_expence(conn, data=data)
    return redirect(url_for('main.expenses'))


@main.route('/expenses', methods=["GET"])
def expenses():
    with get_connection() as conn:
        categories = get_categories(conn)
        currencies = get_currencies(conn)
        expenses = get_expenses(conn)
    return render_template('expenses.html',
                           expenses=expenses,
                           categories=categories,
                           currencies=currencies)


@main.route('/add_new_category', methods=["POST"])
def add_new_category():
    with get_connection() as conn:
        form_values = request.form.to_dict()
        new_category = form_values['new_category'].strip()
        add_category(conn, new_category)
        flash('Категория добавлена', 'success')
    return redirect(url_for('main.categories', new_category=new_category))


@main.route('/categories', methods=["GET"])
def categories(new_category=''):
    with get_connection() as conn:
        categories = get_categories(conn)
    return render_template("categories.html",
                           categories=categories,
                           new_category=new_category)


@main.route('/add_new_currency', methods=["POST"])
def add_new_currency():
    with get_connection() as conn:
        form_values = request.form.to_dict()
        new_currency = form_values['new_currency'].strip()
        add_currency(conn, new_currency)
        flash('Валюта добавлена', 'success')
    return redirect(url_for('main.currencies', new_currency=new_currency))


@main.route('/currencies', methods=["GET"])
def currencies(new_currency=''):
    with get_connection() as conn:
        currencies = get_currencies(conn)
    return render_template("currencies.html",
                           currencies=currencies,
                           new_currency=new_currency)
