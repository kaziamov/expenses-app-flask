from flask import Flask
from datetime import timedelta
from expenses_app.views import main


app = Flask(__name__)
app.secret_key = 'test'
app.url_map.strict_slashes = False
app.permanent_session_lifetime = timedelta(hours=24)
app.register_blueprint(main)


if __name__ == '__main__':
    app()
