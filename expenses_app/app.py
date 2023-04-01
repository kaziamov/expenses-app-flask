from datetime import timedelta

from flask import Flask, render_template, request, flash, redirect

from expenses_app.models import create_currency, create_category, add_new_expence


app = Flask(__name__)
app.secret_key = 'test'
app.url_map.strict_slashes = False
app.permanent_session_lifetime = timedelta(hours=24)


@app.route('/', methods=["GET", "POST"])
def root():
    if request.method == 'POST':
        f = request.form.to_dict()
        data = (f['name'], f["sum"], f["date"], f['currency'], f["category"], f['is_income'])
        add_new_expence(data=data)
    return render_template('home.html')


@app.route('/categories', methods=["GET", "POST"])
def categories():
    return render_template("categories.html")


@app.route('/expenses', methods=["GET", "POST"])
def expenses():
    return render_template("expenses.html")


if __name__ == "__main__":
    app()