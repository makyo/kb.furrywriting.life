from contextlib import closing
import csv
import os
import re

from kbfwlife import connect_db


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


def slugify(text):
    return re.sub(r'\W+', '-', text.lower())

def load(fixture_id):
    with open('fixtures/knowledgebase-{}.csv'.format(fixture_id), 'r') as f:
        fixture = csv.DictReader(f)
        with closing(connect_db()) as db:
            for row in fixture:
                cur = db.cursor()
                user_exists = cur.execute(
                    'select * from users where username = ?',
                    (row['Name'],)).fetchone() is not None
                if not user_exists:
                    cur.execute('insert into users values(?)', (row['Name'],))
                user = row['Name']
                category_exists = cur.execute(
                    'select slug from categories where slug = ?',
                    (slugify(row['Category']),)).fetchone() is not None
                if not category_exists:
                    cur.execute(
                        'insert into categories values(?, ?)',
                        (slugify(row['Category']), row['Category']))
                category = slugify(row['Category'])
                cur.execute('''
                    insert into expertise (
                        user, expertise, content_warning)
                    values(?, ?, ?)''',
                    (user, row['Text'], row['Content Warning'] == 'yes'))
                expertise_id = cur.lastrowid
                topics = re.split(r';\s*', row['Topics'])
                for topic in topics:
                    topic_exists = db.execute(
                        'select id from topics where slug = ? and category = ?',
                        (slugify(topic), category)).fetchone()
                    if topic_exists is None:
                        cur = db.execute('''
                            insert into topics (
                                slug, topic, category)
                            values(?, ?, ?)''',
                            (slugify(topic), topic, category))
                        topic_id = cur.lastrowid
                    else:
                        topic_id = topic_exists[0]
                    cur.execute('''
                        insert into topicexpertise (
                            topic, expertise)
                        values(?, ?)''',
                        (topic_id, expertise_id))
                db.commit()
