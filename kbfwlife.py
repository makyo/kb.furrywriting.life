import os
import sqlite3

from flask import (
    Flask,
    Response,
    g,
    redirect,
    render_template,
    request,
    session,
)

from api import api


# Config
DATABASE = 'knowledgebase.db'
DEBUG = True
SECRET_KEY = 'development key'

# App initialization
app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(api, url_prefix='/api')


# Database initialization
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = base64.b64encode(os.urandom(12))
    return session['_csrf_token']


app.jinja_env.globals['csrf_token'] = generate_csrf_token


@app.before_request
def before_request():
    if request.method == 'POST':
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            return render_template('error.jinja2', error='Token expired :(')
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def front(path):
    return render_template('app.jinja2')


if __name__ == '__main__':
    app.run()
