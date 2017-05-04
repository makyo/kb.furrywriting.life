import os
import sqlite3
from contextlib import closing

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
DATABASE = 'dev.db'
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


def migrate():
    migrations_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'migrations')
    with closing(connect_db()) as db:
        for filename in os.listdir(migrations_dir):
            with open(os.path.join(migrations_dir, filename), 'rb') as f:
                try:
                    db.cursor().executescript(f.read().decode('utf-8'))
                except Exception as e:
                    print('Got {} - maybe already applied?'.format(e))
                finally:
                    pass


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


@app.route('/')
def front():
    return render_template('app.jinja2')


if __name__ == '__main__':
    migrate()
    with closing(connect_db()) as db:
        with open('fixtures.sql', 'rb') as f:
            try:
                db.cursor().executescript(f.read().decode('utf-8'))
            except Exception as e:
                print('Got {} - maybe already applied?'.format(e))
            finally:
                pass
    app.run()
