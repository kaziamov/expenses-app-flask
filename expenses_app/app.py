from datetime import timedelta

from flask import Flask, render_template, request, flash, redirect

from expenses_app.models import create_currency, create_category, add_new_expence
from expenses_app.db_connect import get_connection


app = Flask(__name__)
app.secret_key = 'test'
app.url_map.strict_slashes = False
app.permanent_session_lifetime = timedelta(hours=24)


@app.route('/', methods=["GET", "POST"])
def root():
    if request.method == 'POST':
        f = request.form.to_dict()
        data = (f['name'], f["sum"], f["date"], f['currency'], f["category"], f['is_income'])
        with get_connection() as conn:
            add_new_expence(conn, data=data)
    return render_template('home.html')


@app.route('/categories', methods=["GET", "POST"])
def categories():
    if request.method == 'POST':
        new_category = request.form.get('new_category').strip()
        create_category(new_category)
    flash('Категория добавлена', 'success')
    return render_template("categories.html")


@app.route('/expenses', methods=["GET", "POST"])
def expenses():
    return render_template("expenses.html")


if __name__ == "__main__":
    app()