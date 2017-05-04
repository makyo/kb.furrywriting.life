import json
from flask import (
    Blueprint,
    g,
    json
)


api = Blueprint('api', __name__)


@api.route('/categories')
def get_categories():
    result = {
        'error': '',
        'results': [],
    }
    cur = g.db.execute('select * from categories')
    for row in cur:
        result['results'].append({
            'slug': row[0],
            'category': row[1],
        })
    return json.jsonify(result)


@api.route('/category/<category>')
def get_category(category):
    result = {
        'error': '',
        'result': {},
    }
    row = g.db.execute('select * from categories where slug = ?',
                       (category,)).fetchone()
    if row is not None:
        result['result'] = {
            'slug': row[0],
            'category': row[1],
        }
    else:
        result['error'] = 'category not found'
    return json.jsonify(result)


@api.route('/category/<category>/topics')
def get_topics(category):
    result = {
        'error': '',
        'results': [],
    }
    category_exists = g.db.execute('select * from categories where slug = ?',
                                   (category,)).fetchone() is not None
    if not category_exists:
        result['error'] = 'category not found'
        return json.jsonify(result)
    cur = g.db.execute('''
        select
            topics.slug,
            topics.topic,
            topics.category,
            categories.category
        from topics
            join categories on topics.category = categories.slug
        where topics.category = ?''', (category,))
    for row in cur:
        result['results'].append({
            'slug': row[0],
            'topic': row[1],
            'category_slug': row[2],
            'category': row[3],
        })
    return json.jsonify(result)


@api.route('/category/<category>/topic/<topic>')
def get_topic(category, topic):
    result = {
        'error': '',
        'results': [],
    }
    topic_exists = g.db.execute('select * from topics where slug = ?',
                                (topic,)).fetchone() is not None
    if not topic_exists:
        result['error'] = 'topic not found'
        return json.jsonify(result)
    cur = g.db.execute('''
        select
            expertise.id,
            expertise.expertise,
            topics.topic,
            categories.category,
            users.username
        from expertise
            join topics on topics.slug = expertise.topic
            join categories on categories.slug = topics.category
            join users on users.username = expertise.user
        where topics.category = ? and topics.slug = ?''',
        (category, topic))
    for row in cur:
        result['results'].append({
            'expertise_id': row[0],
            'expertise': row[1],
            'topic_slug': topic,
            'topic': row[2],
            'category_slug': category,
            'category': row[3],
            'user': row[4],
        })
    return json.jsonify(result)


@api.route('/users')
def get_users():
    result = {
        'error': '',
        'results': [],
    }
    cur = g.db.execute('select username from users')
    for row in cur:
        result['results'].append({
            'username': row[0],
        })
    return json.jsonify(result)


@api.route('/user/<user>')
def get_user(user):
    result = {
        'error': '',
        'results': []
    }
    user_exists = g.db.execute('select * from users where username = ?',
                               (user,)).fetchone() is not None
    if not user_exists:
        result['error'] = 'user not found'
        return json.jsonify(result)
    cur = g.db.execute('''
        select
            expertise.id,
            expertise.expertise,
            topics.slug,
            topics.topic,
            categories.slug,
            categories.category
        from expertise
            join topics on expertise.topic = topics.slug
            join categories on topics.category = categories.slug
            join users on expertise.user = users.username
        where expertise.user = ?''',
        (user,))
    for row in cur:
        result['results'].append({
            'expertise_id': row[0],
            'expertise': row[1],
            'topic_slug': row[2],
            'topic': row[3],
            'category_slug': row[4],
            'category': row[5],
            'user': user,
        })
    return json.jsonify(result)
