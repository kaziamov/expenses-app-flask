from datetime import timedelta

from flask import Flask, render_template, request, flash, redirect, url_for

from expenses_app.models import (add_currency,
                                 add_category,
                                 add_new_expence,
                                 get_categories,
                                 get_currencies)
from expenses_app.db_connect import get_connection


app = Flask(__name__)
app.secret_key = 'test'
app.url_map.strict_slashes = False
app.permanent_session_lifetime = timedelta(hours=24)


@app.route('/', methods=["GET", "POST"])
def root():
    return redirect(url_for('expenses'))


@app.route('/expenses', methods=["GET", "POST"])
def expenses():
    if request.method == 'POST':
        form_values = request.form.to_dict()
        data = (form_values['name'],
                form_values["sum"],
                form_values["date"],
                form_values['currency'],
                form_values["category"],
                form_values['is_income'])
        with get_connection() as conn:
            add_new_expence(conn, data=data)
    return render_template('expenses.html')


@app.route('/categories', methods=["GET", "POST"])
def categories():
    new_category = ''
    with get_connection() as conn:
        if request.method == 'POST':
            form_values = request.form.to_dict()
            new_category = form_values['new_category'].strip()
            add_category(conn, new_category)
            flash('Категория добавлена', 'success')
        categories = get_categories(conn)
    return render_template("categories.html",
                           categories=categories,
                           new_category=new_category)


@app.route('/currencies', methods=["GET", "POST"])
def currencies():
    new_currency = ''
    with get_connection() as conn:
        if request.method == 'POST':
            form_values = request.form.to_dict()
            new_currency = form_values['new_currency'].strip()
            add_currency(conn, new_currency)
            flash('Валюта добавлена', 'success')
        currencies = get_currencies(conn)
    return render_template("currencies.html",
                           currencies=currencies,
                           new_currency=new_currency)


if __name__ == "__main__":
    app()
