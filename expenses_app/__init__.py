from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'test'
app.url_map.strict_slashes = False
app.permanent_session_lifetime = timedelta(hours=24)
